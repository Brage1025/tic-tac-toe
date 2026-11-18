# Tic-Tac-Toe

A simple tic-tac-toe game to play in your browser or in the Python console.

**[Play online](https://brage1025.github.io/tic-tac-toe/)** (available after
the first successful GitHub Pages deployment).

## Browser game

- You play as **O**; the computer plays as **X** and starts in the center.
- Select an empty square to make a move.
- Choose **New game** to start over.

Open [`index.html`](index.html) in a browser to play locally. No installation
or build tools are needed. Alternatively, start a local web server:

```powershell
py -m http.server 8000
```

Then open <http://localhost:8000>.

## Python console game

Run the game with Python:

```powershell
py tic_tac_toe.py
```

Enter a number from 1 to 9 to place **O**. The numbers represent the squares
from left to right, top to bottom. The computer plays **X**.

## GitHub Pages

This repository deploys the static browser game to GitHub Pages using GitHub
Actions. Push changes to `main` to publish them. To check a deployment, open
the repository's **Actions** tab; when it succeeds, the game is available at
the link above.

## License

This project is available under the [MIT License](LICENSE).
