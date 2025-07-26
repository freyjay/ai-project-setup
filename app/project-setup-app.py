#!/usr/bin/env python3
"""
Project Setup Automation App
Creates new projects with Claude & Cursor integration
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import shutil
import subprocess
import json
import sys
from pathlib import Path

class ProjectSetupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Setup Automation")
        self.root.geometry("400x408")
        self.root.resizable(False, False)
        
        # Configuration
        self.developer_dir = str(Path.home() / "Developer")
        self.template_dir = str(Path.home() / "Developer" / "project-template-minimal")
        self.config_file = "git-accounts.json"
        
        # Load Git accounts
        self.git_accounts = self.load_git_accounts()
        
        # Create GUI
        self.create_widgets()
        
    def load_git_accounts(self):
        """Load Git accounts from configuration file"""
        default_accounts = {
            "freyjay": {
                "name": "freyjay",
                "email": "francisrey@example.com",
                "ssh_host": "github-personal",
                "ssh_key": "~/.ssh/id_rsa_personal"
            }
        }
        
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except:
                return default_accounts
        else:
            # Create default config file
            with open(self.config_file, 'w') as f:
                json.dump(default_accounts, f, indent=2)
            return default_accounts
    
    def create_widgets(self):
        """Create the GUI widgets"""
        # Bring window to front and focus
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.after(100, lambda: self.root.attributes('-topmost', False))
        
        # Main frame
        main_frame = ttk.Frame(self.root, padding="40")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="🚀 Project Setup Automation", 
                               font=("Arial", 18, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 25))
        
        # Project name
        ttk.Label(main_frame, text="What name do you want for your new project?").grid(
            row=1, column=0, sticky=tk.W, pady=(0, 5))
        self.project_name_var = tk.StringVar()
        self.project_name_entry = ttk.Entry(main_frame, textvariable=self.project_name_var, 
                                           width=40, font=("Arial", 12))
        self.project_name_entry.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        # Directory info
        dir_info = f"Saving it in default Developer directory:\n{self.developer_dir}"
        ttk.Label(main_frame, text=dir_info, foreground="gray").grid(
            row=3, column=0, columnspan=2, sticky=tk.W, pady=(0, 20))
        
        # Git repository selection
        ttk.Label(main_frame, text="Which Git repository do you want it to connect to?").grid(
            row=4, column=0, sticky=tk.W, pady=(0, 5))
        
        self.git_account_var = tk.StringVar()
        self.git_combo = ttk.Combobox(main_frame, textvariable=self.git_account_var, 
                                     state="readonly", width=37, font=("Arial", 12))
        self.git_combo['values'] = list(self.git_accounts.keys())
        if self.git_accounts:
            self.git_combo.set(list(self.git_accounts.keys())[0])
        self.git_combo.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        # Account info display
        self.account_info_var = tk.StringVar()
        self.account_info_label = ttk.Label(main_frame, textvariable=self.account_info_var, 
                                           foreground="blue", font=("Arial", 10))
        self.account_info_label.grid(row=6, column=0, columnspan=2, sticky=tk.W, pady=(0, 20))
        self.update_account_info()
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=7, column=0, columnspan=2, pady=(40, 0))
        
        # Create project button
        self.create_btn = ttk.Button(button_frame, text="Create Project", 
                                    command=self.create_project)
        self.create_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Manage accounts button
        ttk.Button(button_frame, text="Manage Git Accounts", 
                  command=self.manage_accounts).pack(side=tk.LEFT)
        
        # Bind events
        self.git_combo.bind('<<ComboboxSelected>>', self.update_account_info)
        self.root.bind('<Return>', lambda e: self.create_project())
        
        # Set focus to project name entry with multiple attempts
        self.project_name_entry.focus_set()
        self.project_name_entry.focus_force()
        self.root.after(50, lambda: self.project_name_entry.focus_set())
        self.root.after(150, lambda: self.project_name_entry.focus_force())
        
    def update_account_info(self, event=None):
        """Update the account info display"""
        selected_account = self.git_account_var.get()
        if selected_account and selected_account in self.git_accounts:
            account = self.git_accounts[selected_account]
            info = f"Account: {account['name']} | Email: {account['email']} | SSH: {account['ssh_host']}"
            self.account_info_var.set(info)
        else:
            self.account_info_var.set("")
    
    def create_project(self):
        """Create the new project"""
        project_name = self.project_name_var.get().strip()
        git_account = self.git_account_var.get()
        
        # Validation
        if not project_name:
            messagebox.showerror("Error", "Please enter a project name!")
            return
        
        if not git_account:
            messagebox.showerror("Error", "Please select a Git account!")
            return
        
        # Check if project already exists
        project_path = os.path.join(self.developer_dir, project_name)
        if os.path.exists(project_path):
            messagebox.showerror("Error", f"Project '{project_name}' already exists!")
            return
        
        # Check if template exists
        if not os.path.exists(self.template_dir):
            messagebox.showerror("Error", f"Template directory not found:\n{self.template_dir}")
            return
        
        try:
            # Create project directory
            os.makedirs(project_path)
            
            # Copy template files
            self.copy_template_files(project_path)
            
            # Customize files with project info
            self.customize_files(project_path, project_name, git_account)
            
            # Add project to allowed repositories list
            self.add_project_to_allowed_repos(project_name)
            
            # Initialize Git repository
            self.initialize_git(project_path, git_account)
            
            # Success message
            messagebox.showinfo("Success", 
                              f"Project '{project_name}' created successfully!\n\n"
                              f"Location: {project_path}\n\n"
                              f"Next steps:\n"
                              f"1. Open in Cursor: cursor .\n"
                              f"2. Start developing!")
            
            # Close app and terminal after success message
            self.root.quit()
            self.root.destroy()
            
            # Note: Terminal window will remain open - user can close manually if desired
            # This avoids requiring accessibility permissions for automated UI control
            
            sys.exit(0)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create project:\n{str(e)}")
    
    def add_project_to_allowed_repos(self, project_name):
        """Add new project to the allowed repositories list"""
        git_accounts_file = os.path.join(self.developer_dir, ".git-accounts")
        if os.path.exists(git_accounts_file):
            try:
                with open(git_accounts_file, 'r') as f:
                    content = f.read()
                
                # Find the freyjay line and add the new project
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if line.startswith('freyjay|'):
                        # Add the new project to the repositories list
                        if project_name not in line:
                            # Remove the trailing part and add the new project
                            parts = line.split('|')
                            if len(parts) >= 5:
                                repos = parts[4].split(',')
                                if project_name not in repos:
                                    repos.append(project_name)
                                    parts[4] = ','.join(repos)
                                    lines[i] = '|'.join(parts)
                
                # Write back the updated content
                with open(git_accounts_file, 'w') as f:
                    f.write('\n'.join(lines))
                    
            except Exception as e:
                print(f"Warning: Could not update allowed repositories: {e}")
    
    def copy_template_files(self, project_path):
        """Copy template files to new project"""
        # Copy all files and directories from template
        for item in os.listdir(self.template_dir):
            src = os.path.join(self.template_dir, item)
            dst = os.path.join(project_path, item)
            
            if os.path.isdir(src):
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)
    
    def customize_files(self, project_path, project_name, git_account):
        """Customize files with project-specific information"""
        account = self.git_accounts[git_account]
        
        # Files to customize
        files_to_customize = [
            "CLAUDE.md",
            "README.md", 
            ".cursorrules",
            "config/commands.md",
            "config/stack.md",
            "config/environment.md"
        ]
        
        for filename in files_to_customize:
            filepath = os.path.join(project_path, filename)
            if os.path.exists(filepath):
                # Read file content
                with open(filepath, 'r') as f:
                    content = f.read()
                
                # Replace placeholders
                content = content.replace("[PROJECT_NAME]", project_name)
                content = content.replace("[PROJECT_DESCRIPTION]", f"{project_name} - A new project")
                content = content.replace("[REPOSITORY_URL]", f"git@{account['ssh_host']}:{account['name']}/{project_name}.git")
                content = content.replace("[PACKAGE_MANAGER]", "npm")
                content = content.replace("[DEV_COMMAND]", "npm run dev")
                content = content.replace("[LANGUAGE]", "JavaScript/TypeScript")
                content = content.replace("[RUNTIME]", "Node.js")
                
                # Write back
                with open(filepath, 'w') as f:
                    f.write(content)
    
    def initialize_git(self, project_path, git_account):
        """Initialize Git repository with proper error handling"""
        account = self.git_accounts[git_account]
        
        # Change to project directory
        original_dir = os.getcwd()
        os.chdir(project_path)
        
        try:
            # Initialize Git (no check=True to avoid crashes)
            subprocess.run(["git", "init"], capture_output=True)
            
            # Set Git configuration
            subprocess.run(["git", "config", "user.name", account['name']], capture_output=True)
            subprocess.run(["git", "config", "user.email", account['email']], capture_output=True)
            
            # Add remote origin
            remote_url = f"git@{account['ssh_host']}:{account['name']}/{self.project_name_var.get()}.git"
            subprocess.run(["git", "remote", "add", "origin", remote_url], capture_output=True)
            
            # Check if there are files to commit
            result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
            if result.stdout.strip():  # Only commit if there are changes
                subprocess.run(["git", "add", "."], capture_output=True)
                commit_result = subprocess.run(["git", "commit", "-m", "Initial setup: Claude & Cursor environment"], 
                                             capture_output=True, text=True)
                if commit_result.returncode != 0:
                    print(f"Git commit warning: {commit_result.stderr}")
            else:
                # Create a placeholder file if no files exist
                with open("README.md", "w") as f:
                    f.write(f"# {self.project_name_var.get()}\n\nInitial project setup.")
                subprocess.run(["git", "add", "."], capture_output=True)
                commit_result = subprocess.run(["git", "commit", "-m", "Initial setup: Claude & Cursor environment"], 
                                             capture_output=True, text=True)
                if commit_result.returncode != 0:
                    print(f"Git commit warning: {commit_result.stderr}")
            
        except Exception as e:
            # If any Git operations fail, don't crash the app
            print(f"Git initialization warning: {e}")
            # Continue without Git setup - project is still created
        finally:
            os.chdir(original_dir)
    
    def manage_accounts(self):
        """Open account management window"""
        AccountManagerWindow(self.root, self.git_accounts, self.config_file)
        # Reload accounts after potential changes
        self.git_accounts = self.load_git_accounts()
        self.git_combo['values'] = list(self.git_accounts.keys())
        if self.git_accounts:
            self.git_combo.set(list(self.git_accounts.keys())[0])
        self.update_account_info()


class AccountManagerWindow:
    def __init__(self, parent, accounts, config_file):
        self.window = tk.Toplevel(parent)
        self.window.title("Manage Git Accounts")
        self.window.geometry("600x400")
        self.window.resizable(False, False)
        
        self.accounts = accounts.copy()
        self.config_file = config_file
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create account management widgets"""
        # Main frame
        main_frame = ttk.Frame(self.window, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Manage Git Accounts", 
                               font=("Arial", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Accounts list
        ttk.Label(main_frame, text="Current Accounts:").grid(row=1, column=0, sticky=tk.W)
        
        # Listbox for accounts
        self.accounts_listbox = tk.Listbox(main_frame, height=8, width=50)
        self.accounts_listbox.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        self.update_accounts_list()
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=(10, 0))
        
        ttk.Button(button_frame, text="Add Account", command=self.add_account).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(button_frame, text="Edit Account", command=self.edit_account).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(button_frame, text="Remove Account", command=self.remove_account).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(button_frame, text="Save & Close", command=self.save_and_close).pack(side=tk.LEFT)
    
    def update_accounts_list(self):
        """Update the accounts listbox"""
        self.accounts_listbox.delete(0, tk.END)
        for name, account in self.accounts.items():
            self.accounts_listbox.insert(tk.END, f"{name} ({account['email']})")
    
    def add_account(self):
        """Add a new account"""
        self.show_account_dialog()
    
    def edit_account(self):
        """Edit selected account"""
        selection = self.accounts_listbox.curselection()
        if selection:
            account_name = list(self.accounts.keys())[selection[0]]
            self.show_account_dialog(account_name)
        else:
            messagebox.showwarning("Warning", "Please select an account to edit!")
    
    def remove_account(self):
        """Remove selected account"""
        selection = self.accounts_listbox.curselection()
        if selection:
            account_name = list(self.accounts.keys())[selection[0]]
            if messagebox.askyesno("Confirm", f"Remove account '{account_name}'?"):
                del self.accounts[account_name]
                self.update_accounts_list()
        else:
            messagebox.showwarning("Warning", "Please select an account to edit!")
    
    def show_account_dialog(self, account_name=None):
        """Show account dialog for adding/editing"""
        dialog = tk.Toplevel(self.window)
        dialog.title("Add Account" if account_name is None else "Edit Account")
        dialog.geometry("400x300")
        dialog.resizable(False, False)
        
        # Form fields
        ttk.Label(dialog, text="Account Name:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        name_var = tk.StringVar(value=account_name or "")
        name_entry = ttk.Entry(dialog, textvariable=name_var, width=30)
        name_entry.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
        
        ttk.Label(dialog, text="Email:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        email_var = tk.StringVar(value=self.accounts.get(account_name, {}).get('email', ""))
        email_entry = ttk.Entry(dialog, textvariable=email_var, width=30)
        email_entry.grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)
        
        ttk.Label(dialog, text="SSH Host:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        ssh_host_var = tk.StringVar(value=self.accounts.get(account_name, {}).get('ssh_host', ""))
        ssh_host_entry = ttk.Entry(dialog, textvariable=ssh_host_var, width=30)
        ssh_host_entry.grid(row=2, column=1, sticky=tk.W, padx=10, pady=5)
        
        ttk.Label(dialog, text="SSH Key:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        ssh_key_var = tk.StringVar(value=self.accounts.get(account_name, {}).get('ssh_key', ""))
        ssh_key_entry = ttk.Entry(dialog, textvariable=ssh_key_var, width=30)
        ssh_key_entry.grid(row=3, column=1, sticky=tk.W, padx=10, pady=5)
        
        def save_account():
            name = name_var.get().strip()
            email = email_var.get().strip()
            ssh_host = ssh_host_var.get().strip()
            ssh_key = ssh_key_var.get().strip()
            
            if not all([name, email, ssh_host, ssh_key]):
                messagebox.showerror("Error", "All fields are required!")
                return
            
            # Remove old account if editing
            if account_name and account_name != name:
                del self.accounts[account_name]
            
            # Add/update account
            self.accounts[name] = {
                'name': name,
                'email': email,
                'ssh_host': ssh_host,
                'ssh_key': ssh_key
            }
            
            self.update_accounts_list()
            dialog.destroy()
        
        # Save button
        ttk.Button(dialog, text="Save", command=save_account).grid(row=4, column=0, columnspan=2, pady=20)
    
    def save_and_close(self):
        """Save accounts and close window"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.accounts, f, indent=2)
            self.window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save accounts:\n{str(e)}")


def main():
    """Main application entry point"""
    root = tk.Tk()
    
    # Configure style
    style = ttk.Style()
    style.theme_use('clam')
    
    # Create and run app
    app = ProjectSetupApp(root)
    
    # Center window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    # Set focus to project name entry after window is fully loaded
    def set_final_focus():
        app.project_name_entry.focus_force()
        app.project_name_entry.selection_range(0, tk.END)
    
    root.after(300, set_final_focus)
    
    root.mainloop()


if __name__ == "__main__":
    main()
