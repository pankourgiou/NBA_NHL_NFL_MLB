import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def generate_sport_data(sport, n_players):
    np.random.seed(hash(sport) % 10000)  # different seed per sport
    if sport == "NBA":
        return pd.DataFrame({
            "Points": np.random.normal(15, 5, n_players),
            "Assists": np.random.normal(5, 2, n_players),
            "Rebounds": np.random.normal(7, 3, n_players),
            "Blocks": np.random.normal(1, 0.5, n_players),
            "Steals": np.random.normal(1.5, 0.6, n_players),
            "Sport": sport
        })
    elif sport == "NHL":
        return pd.DataFrame({
            "Goals": np.random.normal(20, 10, n_players),
            "Assists": np.random.normal(30, 12, n_players),
            "Hits": np.random.normal(80, 25, n_players),
            "Blocks": np.random.normal(40, 15, n_players),
            "Sport": sport
        })
    elif sport == "MLB":
        return pd.DataFrame({
            "HomeRuns": np.random.normal(20, 10, n_players),
            "RBIs": np.random.normal(70, 30, n_players),
            "Hits": np.random.normal(130, 20, n_players),
            "StolenBases": np.random.normal(15, 10, n_players),
            "Sport": sport
        })
    elif sport == "NFL":
        return pd.DataFrame({
            "Touchdowns": np.random.normal(10, 5, n_players),
            "Yards": np.random.normal(800, 200, n_players),
            "Interceptions": np.random.normal(5, 2, n_players),
            "Tackles": np.random.normal(50, 15, n_players),
            "Sport": sport
        })
    else:
        return pd.DataFrame()

# --- Combine all sports ---
nba = generate_sport_data("NBA", 100)
nhl = generate_sport_data("NHL", 100)
mlb = generate_sport_data("MLB", 100)
nfl = generate_sport_data("NFL", 100)

df = pd.concat([nba, nhl, mlb, nfl], ignore_index=True)
df.fillna(0, inplace=True)  # Fill missing stats with 0

# --- Preprocess features ---
features = df.drop(columns=["Sport"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# --- Approximate t-SimCNE with t-SNE (Student-t kernel based) ---
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, metric="euclidean", random_state=42)
X_embedded = tsne.fit_transform(X_scaled)

# --- Plot ---
plt.figure(figsize=(10, 6))
colors = {"NBA": "red", "NHL": "blue", "MLB": "green", "NFL": "purple"}
for sport in colors:
    idx = df["Sport"] == sport
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=colors[sport], label=sport, alpha=0.7)

plt.legend()
plt.title("t-SimCNE (approximate with t-SNE) - Player Stat Embeddings")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()
