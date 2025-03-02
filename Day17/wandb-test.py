import pandas as pd
import wandb

# Load dataset
data = pd.read_csv("Day17/advertising (1).csv", encoding="utf-8")
dataset = data[['TV', 'Radio', 'Newspaper', 'Sales']]

b = 1
w1 = w2 = w3 = 0
lr = 0.000001  
epochs = 1000
print(data.head(5))
print(data.tail(5))

wandb.init(project="demo-linear-regression", config={"learning_rate": lr, "epochs": epochs})
wandb.log({"Dataset": wandb.Table(dataframe=dataset)})

X1_train = dataset['TV']
X2_train = dataset['Radio']
X3_train = dataset['Newspaper']
Y_train = dataset['Sales']
N = len(X1_train)

def predict(x1, x2, x3, w1, w2, w3, b):
    return x1 * w1 + x2 * w2 + x3 * w3 + b

def gradient(y_hat, y, x1, x2, x3):
    dw1 = 2 * (y_hat - y) * x1
    dw2 = 2 * (y_hat - y) * x2
    dw3 = 2 * (y_hat - y) * x3
    db = 2 * (y_hat - y)
    return dw1, dw2, dw3, db

def update_weight(w1, w2, w3, b, lr, dw1, dw2, dw3, db):
    w1 -= lr * dw1
    w2 -= lr * dw2
    w3 -= lr * dw3
    b -= lr * db
    return w1, w2, w3, b

for epoch in range(epochs):
    losses = []  
    for i in range(N):
        x1 = X1_train.iloc[i]
        x2 = X2_train.iloc[i]
        x3 = X3_train.iloc[i]
        y = Y_train.iloc[i]

        y_hat = predict(x1, x2, x3, w1, w2, w3, b)

        loss = (y_hat - y) ** 2 
        wandb.log({"loss": loss})
        
        dw1, dw2, dw3, db = gradient(y_hat, y, x1, x2, x3)

        w1, w2, w3, b = update_weight(w1, w2, w3, b, lr, dw1, dw2, dw3, db)

        losses.append(loss)

    wandb.log({"epoch_loss": sum(losses) / len(losses)})

wandb.finish()
