CREATE TABLE
  users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid (),
    username TEXT,
    email TEXT UNIQUE,git merge --no-ff
    password TEXT,
	phone INTEGER,
	age INTEGER,
	major TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW (),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW ()
  );

CREATE TABLE
  skills (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid (),
    name TEXT,
    description TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW (),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW ()
  );

CREATE TABLE
  courses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid (),
    title TEXT,
    description TEXT,
    instr TEXT,
	phone INTEGER,
	age INTEGER,
	major TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW (),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW ()
  );

CREATE TABLE
  user_skills (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid (),
    user_id UUID REFERENCES users (id) ON DELETE CASCADE,
    input_text TEXT,
    sentiment_label TEXT,
    confidence_score TEXT,
    last_analysis_at TIMESTAMP,
    created_at TIMESTAMP NOT NULL DEFAULT NOW (),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW ()
  );

CREATE TABLE
  model_performance (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid (),
    model_version TEXT,
    accuracy TEXT,
    fl_score INTEGER,
    training_date TIMESTAMP NOT NULL DEFAULT NOW (),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW (),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW ()
  );

