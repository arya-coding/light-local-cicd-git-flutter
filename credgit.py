GITHUB_TOKEN = ''

# Creating a GitHub Personal Access Token (PAT) with Specific Repository Access
# --------------------------------------------------------------------------------
# Step 1: Sign in to GitHub
# - Navigate to https://github.com and log in to your account.

# Step 2: Accessing Token Settings
# - After logging in, click on your profile picture at the top right.
# - Select "Settings" from the dropdown menu.
# - On the left sidebar, click on "Developer settings".
# - Under "Developer settings", click on "Personal access tokens".

# Step 3: Generating a New Token
# - Click the "Generate new token" button.
# - Enter a name for your token in the "Note" field to remember its purpose.

# Step 4: Selecting Scopes
# - Here you can set the permissions (scopes) for your token.
# - To minimize security risks, only grant the necessary permissions : Select your repo and authorize pull and content rights.

# Step 5: Generating the Token
# - After setting the desired scopes, scroll down and click "Generate token".
# - Copy the token immediately and store it securely; GitHub won't show it again.

# Step 6: Using the Token in Your Projects
# - Use this token in place of your password when performing Git operations over HTTPS.
# - You can also use it for API requests. For example:
#   curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/user/repos

# Important Security Tips
# - Never share your personal access tokens.
# - Avoid storing tokens in your code, especially if it's public.
# - Regularly review and revoke tokens you no longer use.
# - Consider implementing additional security measures like two-factor authentication.

# Note: If you need to give access to a specific repository only, consider creating a machine user account.
# This account represents a bot or service and has access to only the repositories it needs.
