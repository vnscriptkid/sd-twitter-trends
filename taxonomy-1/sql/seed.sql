-- Development (100)
-- │
-- ├── Web Development (85)
-- │   ├── JavaScript (70)
-- │   ├── React (75)
-- │   └── Node.js (65)
-- │
-- ├── Data Science (80)
-- │   ├── Python (80)
-- │   ├── Machine Learning (85)
-- │   └── Deep Learning (75)
-- │
-- └── Mobile Development (75)
--     ├── Android Development (70)
--     ├── iOS Development (80)
--     └── Flutter (65)

-- Business (95)
-- │
-- ├── Entrepreneurship (85)
-- │   ├── Startup (70)
-- │   ├── Business Strategy (75)
-- │   └── Freelancing (65)
-- │
-- ├── Communication (80)
-- │   ├── Public Speaking (80)
-- │   ├── Presentation Skills (85)
-- │   └── Writing (75)
-- │
-- └── Management (75)
--     ├── Leadership (70)
--     ├── Project Management (75)
--     └── Team Management (65)

-- Finance & Accounting (90)
-- │
-- ├── Accounting & Bookkeeping (85)
-- │   ├── Financial Accounting (80)
-- │   ├── QuickBooks (85)
-- │   └── Tax Preparation (75)
-- │
-- ├── Investing & Trading (80)
-- │   ├── Stock Trading (70)
-- │   ├── Cryptocurrency (75)
-- │   └── Forex (65)
-- │
-- └── Personal Finance (75)
--     ├── Budgeting (80)
--     ├── Retirement Planning (85)
--     └── Investing Basics (75)

-- Categories
INSERT INTO taxonomies (name, parent_id, type, score) VALUES
('Development', NULL, 1, 100),
('Business', NULL, 1, 95),
('Finance & Accounting', NULL, 1, 90);

-- Subcategories for Development
INSERT INTO taxonomies (name, parent_id, type, score) VALUES
('Web Development', 1, 2, 85),
('Data Science', 1, 2, 80),
('Mobile Development', 1, 2, 75);

-- Topics for Web Development
INSERT INTO taxonomies (name, parent_id, type, score) VALUES
('JavaScript', 4, 3, 70),
('React', 4, 3, 75),
('Node.js', 4, 3, 65);

-- Topics for Data Science
INSERT INTO taxonomies (name, parent_id, type, score) VALUES
('Python', 5, 3, 80),
('Machine Learning', 5, 3, 85),
('Deep Learning', 5, 3, 75);

-- Topics for Mobile Development
INSERT INTO taxonomies (name, parent_id, type, score) VALUES
('Android Development', 6, 3, 70),
('iOS Development', 6, 3, 80),
('Flutter', 6, 3, 65);

-- Subcategories for Business
INSERT INTO taxonomies (name, parent_id, type, score) VALUES
('Entrepreneurship', 2, 2, 85),
('Communication', 2, 2, 80),
('Management', 2, 2, 75);

-- Topics for Entrepreneurship
INSERT INTO taxonomies (name, parent_id, type, score) VALUES
('Startup', 16, 3, 70),
('Business Strategy', 16, 3, 75),
('Freelancing', 16, 3, 65);

-- Topics for Communication
INSERT INTO taxonomies (name, parent_id, type, score) VALUES
('Public Speaking', 17, 3, 80),
('Presentation Skills', 17, 3, 85),
('Writing', 17, 3, 75);

-- Topics for Management
INSERT INTO taxonomies (name, parent_id, type, score) VALUES
('Leadership', 18, 3, 70),
('Project Management', 18, 3, 75),
('Team Management', 18, 3, 65);

-- Subcategories for Finance & Accounting
INSERT INTO taxonomies (name, parent_id, type, score) VALUES
('Accounting & Bookkeeping', 3, 2, 85),
('Investing & Trading', 3, 2, 80),
('Personal Finance', 3, 2, 75);

-- Topics for Accounting & Bookkeeping
INSERT INTO taxonomies (name, parent_id, type, score) VALUES
('Financial Accounting', 19, 3, 80),
('QuickBooks', 19, 3, 85),
('Tax Preparation', 19, 3, 75);

-- Topics for Investing & Trading
INSERT INTO taxonomies (name, parent_id, type, score) VALUES
('Stock Trading', 20, 3, 70),
('Cryptocurrency', 20, 3, 75),
('Forex', 20, 3, 65);

-- Topics for Personal Finance
INSERT INTO taxonomies (name, parent_id, type, score) VALUES
('Budgeting', 21, 3, 80),
('Retirement Planning', 21, 3, 85),
('Investing Basics', 21, 3, 75);
