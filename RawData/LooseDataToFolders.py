import os
import shutil
import pandas as pd

# Pfade
source_dir = "train"  # Wo die Bilder jetzt liegen
target_dir = "dataset"           # Zielstruktur
csv_file = "Training_set.csv"              # Deine CSV-Datei

# CSV lesen
df = pd.read_csv(csv_file)

# Bilder umkopieren
for _, row in df.iterrows():
    label = row['label']
    filename = row['filename']
    
    # Zielordner für Label
    label_dir = os.path.join(target_dir, label)
    os.makedirs(label_dir, exist_ok=True)
    
    # Quelle und Ziel
    src = os.path.join(source_dir, filename)
    dst = os.path.join(label_dir, filename)
    
    # Kopieren
    shutil.copy2(src, dst)

print("Umstrukturierung abgeschlossen.")
