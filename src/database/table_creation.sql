CREATE TABLE address (    
    id SERIAL PRIMARY KEY,   
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,    
    zip_code VARCHAR NOT NULL UNIQUE TRUE,
    city VARCHAR NOT NULL,
    state VARCHAR NOT NULL,
    street VARCHAR NULL,
    neighborhood VARCHAR NULL
);