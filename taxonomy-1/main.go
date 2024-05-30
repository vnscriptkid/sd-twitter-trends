package main

import (
	"database/sql"
	"fmt"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
	"gorm.io/gorm/logger"
)

const (
	TypeCategory    = 1
	TypeSubcategory = 2
	TypeTopic       = 3
)

type Taxonomy struct {
	ID       uint       `gorm:"primaryKey"`
	Name     string     `gorm:"not null"`
	ParentID *uint      `gorm:"index"`
	Type     int        `gorm:"not null"`
	Score    int        `gorm:"not null;default:0"`
	Children []Taxonomy `gorm:"foreignKey:ParentID"`
	Parent   *Taxonomy  `gorm:"foreignKey:ParentID"`
}

func main() {
	dsn := "host=localhost user=postgres password=123456 dbname=postgres port=5432 sslmode=disable"
	db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{
		// default logger
		Logger: logger.Default.LogMode(logger.Info),
	})
	if err != nil {
		panic("failed to connect database")
	}

	// Migrate the schema
	err = db.AutoMigrate(&Taxonomy{})

	if err != nil {
		panic("failed to migrate")
	}

	//////////////////////////////////////////
	// UC1: Get topic by ID
	//////////////////////////////////////////
	topic, err := GetTopicByID(db, 9)
	if err != nil {
		panic(err)
	}

	fmt.Println("Topic:", topic.Name)

	topic, err = GetTopicPath(db, 9)
	if err != nil {
		panic(err)
	}

	fmt.Println("\nTopic:", topic.Name)

	//////////////////////////////////////////
	// UC2: Get topic path
	//////////////////////////////////////////
	topic, err = GetTopicPath(db, 9)
	if err != nil {
		panic(err)
	}

	fmt.Println("\nTopic:", topic.Name)
	fmt.Println("Parent:", topic.Parent.Name)
	fmt.Println("Grandparent:", topic.Parent.Parent.Name)

	topic, err = GetTopicPathRaw(db, 9)
	if err != nil {
		panic(err)
	}

	fmt.Println("\nTopic:", topic.Name)
	fmt.Println("Parent:", topic.Parent.Name)
	fmt.Println("Grandparent:", topic.Parent.Parent.Name)
}

// USECASE 1: Get topic by ID
func GetTopicByID(db *gorm.DB, id uint) (*Taxonomy, error) {
	var topic Taxonomy
	err := db.First(&topic, id).Error

	if err != nil {
		return nil, fmt.Errorf("failed to get topic by ID: %w", err)
	}
	return &topic, nil
}

func GetTopicByIDRaw(db *gorm.DB, id uint) (*Taxonomy, error) {
	var topic Taxonomy
	err := db.Raw("SELECT * FROM taxonomies WHERE id = ?", id).Scan(&topic).Error

	if err != nil {
		return nil, fmt.Errorf("failed to get topic by ID: %w", err)
	}

	return &topic, nil
}

// USECASE 2: Get topic path
func GetTopicPath(db *gorm.DB, id uint) (*Taxonomy, error) {
	var topic Taxonomy
	err := db.
		Preload("Parent").
		Preload("Parent.Parent").
		First(&topic, id).Error

	// Fire 3 separate queries
	// SELECT * FROM "taxonomies" WHERE "taxonomies"."id" = 1
	// SELECT * FROM "taxonomies" WHERE "taxonomies"."id" = 4
	// SELECT * FROM "taxonomies" WHERE "taxonomies"."id" = 9 ORDER BY "taxonomies"."id" LIMIT 1

	if err != nil {
		return nil, fmt.Errorf("failed to get topic by ID: %w", err)
	}
	return &topic, nil
}

func GetTopicPathRaw(db *gorm.DB, id uint) (*Taxonomy, error) {
	var taxonomy []Taxonomy
	err := db.Raw(`
		WITH RECURSIVE taxonomy_path AS (
			SELECT 
				id, name, parent_id, type, score
			FROM taxonomies
			WHERE id = @id
			UNION ALL
			SELECT 
				t.id, t.name, t.parent_id, t.type, t.score
			FROM taxonomies t
			INNER JOIN taxonomy_path tp ON t.id = tp.parent_id
		)
		SELECT 
			id, name, parent_id, type, score
		FROM taxonomy_path
		ORDER BY type DESC
	`, sql.Named("id", id)).Scan(&taxonomy).Error

	if err != nil {
		return nil, fmt.Errorf("failed to get topic by ID: %w", err)
	}

	topic := taxonomy[0]
	topic.Parent = &taxonomy[1]
	topic.Parent.Parent = &taxonomy[2]

	return &topic, nil
}
