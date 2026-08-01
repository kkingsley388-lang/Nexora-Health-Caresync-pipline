CREATE ROLE nexora_health_user WITH LOGIN PASSWORD 'data_pipeline';  
CREATE DATABASE nexora_health_database;
GRANT ALL PRIVILEGES ON DATABASE nexora_health_database TO nexora_health_user;
