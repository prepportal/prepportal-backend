CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

SELECT * FROM pg_extension;

-- Create the Branch table
CREATE TABLE branch (
    branch_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    code VARCHAR(10) NOT NULL,
    description TEXT
);

-- Create the SemesterGroup table
CREATE TABLE semestergroup (
    semester_group_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(20) NOT NULL,
    year INT NOT NULL,
    description TEXT
);

-- Create the Semester table
CREATE TABLE semester (
    semester_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(20) NOT NULL,
    number INT NOT NULL,
    semester_group_id UUID REFERENCES semestergroup (semester_group_id) ON DELETE CASCADE,
    description TEXT
);

-- Create the Many-to-Many relationship table between Semester and Branch
CREATE TABLE semester_branch (
    id SERIAL PRIMARY KEY,
    semester_id UUID REFERENCES semester (semester_id) ON DELETE CASCADE,
    branch_id UUID REFERENCES branch (branch_id) ON DELETE CASCADE
);


-- Create the SubjectType table
CREATE TABLE subjecttype (
    subject_type_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(50) NOT NULL,
    description TEXT
);

-- Create the Subject table
CREATE TABLE subject (
    subject_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    code VARCHAR(20) NOT NULL,
    semester_id UUID REFERENCES semester (semester_id) ON DELETE CASCADE,
    subject_type_id UUID REFERENCES subjecttype (subject_type_id) ON DELETE CASCADE,
    description TEXT
);

-- Create the QuestionPaper table
CREATE TABLE questionpaper (
    question_paper_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    month VARCHAR(20) NOT NULL,
    year INT NOT NULL,
    file_id VARCHAR(255) NOT NULL,
    file_size INT NOT NULL,
    file_format VARCHAR(20) NOT NULL,
    thumb TEXT NOT NULL,
    subject_id UUID REFERENCES subject (subject_id) ON DELETE CASCADE,
    description TEXT
);

-- Create the Note table
CREATE TABLE note (
    note_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(255) NOT NULL,
    file_id VARCHAR(255) NOT NULL,
    file_size INT NOT NULL,
    file_format VARCHAR(20) NOT NULL,
    thumb TEXT NOT NULL,
    subject_id UUID REFERENCES subject (subject_id) ON DELETE CASCADE,
    description TEXT
);