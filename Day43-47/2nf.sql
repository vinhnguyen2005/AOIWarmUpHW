-- Cau 1: Primary Key: agent_id va task_id

-- Cau 2: Vi Pham 2NF, do agent_name, llm_model phu thuoc agent_id, va task_name va task_type thi phu thuoc vao task_id

-- Cau 3:
CREATE TABLE Agents (
    agent_id VARCHAR(10) PRIMARY KEY,
    agent_name VARCHAR(100),
    llm_model VARCHAR(50)
);

CREATE TABLE Tasks (
    task_id VARCHAR(10) PRIMARY KEY,
    task_name VARCHAR(100),
    task_type VARCHAR(50)
);

CREATE TABLE AgentTasks (
    agent_id VARCHAR(10),
    task_id VARCHAR(10),
    PRIMARY KEY (agent_id, task_id),
    FOREIGN KEY (agent_id) REFERENCES Agents(agent_id),
    FOREIGN KEY (task_id) REFERENCES Tasks(task_id)
);

INSERT INTO Agents (agent_id, agent_name, llm_model) VALUES
('A01', 'Claude Agent', 'Claude 3'),
('A02', 'GPT Assistant', 'GPT-4'),
('A03', 'Gemini Helper', 'Gemini 1.5');

INSERT INTO Tasks (task_id, task_name, task_type) VALUES
('T01', 'Summarization', 'NLP'),
('T02', 'SQL Generation', 'Code'),
('T03', 'Sentiment Analysis', 'NLP');

INSERT INTO AgentTasks (agent_id, task_id) VALUES
('A01', 'T01'),
('A01', 'T03'),
('A02', 'T02'),
('A03', 'T01');

-- Cau 5
SELECT a.agent_name, t.task_name
FROM AgentTasks at
JOIN Agents a ON at.agent_id = a.agent_id
JOIN Tasks t ON at.task_id = t.task_id;

SELECT llm_model FROM Agents 

SELECT task_type, COUNT(task_type) as taskCount FROM Tasks
GROUP BY task_type

SELECT agent_name FROM Agents WHERE llm_model LIKE 'G%'
