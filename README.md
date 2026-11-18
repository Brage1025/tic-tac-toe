# Tic-Tac-Toe

A small tic-tac-toe game with both a Python console version and a browser
version.

## Play locally

Open `index.html` directly in your web browser. It has no dependencies or build
step.

You can also start a local server from this folder:

```powershell
py -m http.server 8000
```

Then visit <http://localhost:8000>.

## Publish with GitHub Pages

The site is a static webpage, so GitHub Pages can serve it without a build
step. The workflow in `.github/workflows/pages.yml` deploys the repository when
you push to `main`.

1. Create an empty repository on GitHub (do not add a README or other files).
2. From this folder, initialize Git and push the project. Replace the URL with
   your repository's URL:

   ```powershell
   git init
   git add .
   git commit -m "Initial tic-tac-toe game"
   git branch -M main
   git remote add origin https://github.com/<YOUR-USERNAME>/<YOUR-REPOSITORY>.git
   git push -u origin main
   ```

3. In the GitHub repository, open **Settings → Pages** and set the build and
   deployment source to **GitHub Actions**.
4. Open the **Actions** tab and wait for **Deploy to GitHub Pages** to finish.
   The workflow summary shows the published site URL.

Subsequent pushes to `main` deploy automatically. You can also run the workflow
manually from the **Actions** tab.

## Play in the console

Run:

```powershell
py tic_tac_toe.py
```

The computer starts in the center. Enter a number from 1 to 9 to place `O`;
the number corresponds to the square position shown by the console board.
