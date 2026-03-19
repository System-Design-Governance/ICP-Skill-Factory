"""Build .plugin and .skill ZIP packages from 06-plugin-src/."""
import zipfile, os

BASE = os.getcwd()
SRC = os.path.join(BASE, "06-plugin-src")
PLUGIN_OUT = os.path.join(BASE, "05-cowork-skills", "plugins")
PKG_OUT = os.path.join(BASE, "05-cowork-skills", "packages")

# Remove old .plugin and .skill files
for f in os.listdir(PLUGIN_OUT):
    if f.endswith('.plugin'):
        os.remove(os.path.join(PLUGIN_OUT, f))
for f in os.listdir(PKG_OUT):
    if f.endswith('.skill'):
        os.remove(os.path.join(PKG_OUT, f))

# Build .plugin packages
print("=== Building .plugin packages ===")
for plugin_name in sorted(os.listdir(SRC)):
    plugin_dir = os.path.join(SRC, plugin_name)
    if not os.path.isdir(plugin_dir) or not plugin_name.startswith("icp-"):
        continue
    plugin_file = os.path.join(PLUGIN_OUT, f"{plugin_name}.plugin")
    with zipfile.ZipFile(plugin_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(plugin_dir):
            for file in files:
                if file == '.DS_Store':
                    continue
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, plugin_dir)
                zf.write(file_path, arcname)
    skills_dir = os.path.join(plugin_dir, "skills")
    skill_count = len([d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))])
    size_kb = os.path.getsize(plugin_file) / 1024
    print(f"  {plugin_name}.plugin: {skill_count} skills, {size_kb:.0f} KB")

# Build .skill packages
print("\n=== Building .skill packages ===")
skill_total = 0
for plugin_name in sorted(os.listdir(SRC)):
    plugin_dir = os.path.join(SRC, plugin_name)
    if not os.path.isdir(plugin_dir) or not plugin_name.startswith("icp-"):
        continue
    skills_dir = os.path.join(plugin_dir, "skills")
    for skill_name in sorted(os.listdir(skills_dir)):
        skill_dir = os.path.join(skills_dir, skill_name)
        if not os.path.isdir(skill_dir):
            continue
        skill_file = os.path.join(PKG_OUT, f"{skill_name}.skill")
        with zipfile.ZipFile(skill_file, 'w', zipfile.ZIP_DEFLATED) as zf:
            for root, dirs, files in os.walk(skill_dir):
                for file in files:
                    if file == '.DS_Store':
                        continue
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, skill_dir)
                    zf.write(file_path, arcname)
        skill_total += 1

print(f"  Built {skill_total} .skill packages")

# Summary
plugins = [f for f in os.listdir(PLUGIN_OUT) if f.endswith('.plugin')]
skills = [f for f in os.listdir(PKG_OUT) if f.endswith('.skill')]
print(f"\n=== Final Summary ===")
print(f"Plugin packages: {len(plugins)}")
print(f"Skill packages: {len(skills)}")
print("\nPlugin sizes:")
for p in sorted(plugins):
    size = os.path.getsize(os.path.join(PLUGIN_OUT, p))
    print(f"  {p}: {size/1024:.0f} KB")
