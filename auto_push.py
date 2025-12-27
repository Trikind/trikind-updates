import subprocess
import datetime

def run_git_sync():
    """Automates the staging, committing, and pushing of TriKind assets."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    commit_message = f"Automated TriKind Build & Log Update - {timestamp}"
    
    try:
        # Stage all changes (new assets and logs)
        subprocess.run(["git", "add", "."], check=True)
        
        # Commit the changes
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # Push to the main branch
        subprocess.run(["git", "push", "origin", "main"], check=True)
        
        print(f"✅ TriKind Success: Assets and News updated at {timestamp}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Friction Alert: Git sync failed. Error: {e}")

if __name__ == "__main__":
    run_git_sync()
