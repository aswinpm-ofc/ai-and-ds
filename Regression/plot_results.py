import pandas as pd
import matplotlib.pyplot as plt

# Load training history
hist = pd.read_csv("out_reg_csv/training_history.csv")
plt.figure(figsize=(6,4))
plt.plot(hist["epoch"], hist["loss"], marker="o")
plt.xlabel("Epoch")
plt.ylabel("Loss (MSE)")
plt.title("Training loss vs epoch")
plt.grid(True)
plt.tight_layout()
plt.savefig("out_reg_csv/loss_vs_epoch.png", dpi=150)
print("Saved out_reg_csv/loss_vs_epoch.png")

# Load predictions
preds = pd.read_csv("out_reg_csv/predictions_preview.csv")
if {"y_true","y_pred"}.issubset(preds.columns):
    plt.figure(figsize=(6,6))
    plt.scatter(preds["y_true"], preds["y_pred"], alpha=0.7)
    plt.plot([preds["y_true"].min(), preds["y_true"].max()],
             [preds["y_true"].min(), preds["y_true"].max()], linestyle="--")
    plt.xlabel("True score")
    plt.ylabel("Predicted score")
    plt.title("True vs Predicted (test preview)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("out_reg_csv/true_vs_pred.png", dpi=150)
    print("Saved out_reg_csv/true_vs_pred.png")
else:
    print("Cannot plot true vs pred: columns y_true/y_pred missing in predictions_preview.csv")

print("Done.")
