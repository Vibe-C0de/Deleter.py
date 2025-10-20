import os
import shutil

def search_folder(folder_name):
    """Search for folder in common directories"""
    search_paths = [
        os.getcwd(),  # Current directory
        os.path.expanduser("~"),  # Home directory
        os.path.expanduser("~/Desktop"),
        os.path.expanduser("~/Downloads"),
        "C:\\" if os.name == 'nt' else "/",  # Root directory
    ]
    
    found_paths = []
    
    for search_path in search_paths:
        if os.path.exists(search_path):
            for root, dirs, files in os.walk(search_path):
                if folder_name in dirs:
                    full_path = os.path.join(root, folder_name)
                    found_paths.append(full_path)
                # Limit search depth for performance
                if len(found_paths) > 10:
                    break
        if found_paths:
            break
    
    return found_paths

def delete_specific_folder():
    # Ask user for folder name
    target_folder = input("Enter the folder name to search and delete: ").strip()
    
    if not target_folder:
        print("❌ No folder name provided!")
        return
    
    print(f"🔍 Searching for folder: '{target_folder}'...")
    
    # Search for the folder
    found_paths = search_folder(target_folder)
    
    if not found_paths:
        print(f"❌ Folder '{target_folder}' not found in common locations.")
        return
    
    # Show found folders
    print(f"\n📁 Found {len(found_paths)} folder(s):")
    for i, path in enumerate(found_paths, 1):
        print(f"  {i}. {path}")
    
    # Let user choose which one to delete
    if len(found_paths) > 1:
        try:
            choice = input(f"\nSelect folder to delete (1-{len(found_paths)} or 'all'): ").strip()
            if choice.lower() == 'all':
                folders_to_delete = found_paths
            else:
                index = int(choice) - 1
                if 0 <= index < len(found_paths):
                    folders_to_delete = [found_paths[index]]
                else:
                    print("❌ Invalid selection!")
                    return
        except ValueError:
            print("❌ Please enter a valid number!")
            return
    else:
        folders_to_delete = found_paths
    
    # Confirm deletion
    print(f"\n⚠️  WARNING: This will PERMANENTLY delete:")
    for folder in folders_to_delete:
        print(f"    - {folder}")
    
    confirm = input("\nAre you sure? (yes/no): ").strip().lower()
    
    if confirm in ['yes', 'y']:
        # Delete selected folders
        for folder_path in folders_to_delete:
            try:
                if os.path.exists(folder_path):
                    shutil.rmtree(folder_path)
                    print(f"✅ Successfully deleted: {folder_path}")
                else:
                    print(f"❌ Folder not found: {folder_path}")
            except Exception as e:
                print(f"❌ Error deleting {folder_path}: {e}")
    else:
        print("❌ Deletion cancelled.")

if __name__ == "__main__":
    print("🗑️  Advanced Folder Deletion Tool")
    print("=" * 40)
    delete_specific_folder()