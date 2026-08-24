#file to graph all the data
import pandas as pd
import matplotlib.pyplot as plt

#load data
fn = "../results/k_values.csv"
df = pd.read_csv(fn)

print(df.head())

# plot
plt.figure(figsize=(8, 5))
plt.plot(df["k"], df["naive"] * 100, label="Naive (raw one-hot, incl. race/sex)", marker="o")
plt.plot(df["k"], df["smart"] * 100, label="Smart (unscaled numeric)", marker="s")
plt.plot(df["k"], df["smart_scaled"] * 100, label="Smart + Scaled numeric", marker="^")
plt.plot(df["k"], df["smart_scaled_no_demo"] * 100, label="Smart + Scaled, no race/sex", marker="d")
plt.xlabel("k")
plt.ylabel("Dev error rate (%)")
plt.title("HW1: k-NN dev error vs k, by feature/preprocessing approach")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("../results/error_vs_k.png", dpi=150)
plt.show()
