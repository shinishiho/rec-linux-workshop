# Arisu Game

**Arisu Game** lấy cảm hứng từ series Vua trò chơi Arisu từ Game thâu đêm. Cảm ơn anh bạn đã tạo ra một series thật là bruh để tôi có thể tạo ra cái workshop củ chuối này.

**Arisu Game** took inspiration from "Vua trò chơi Arisu" from "Game thâu đêm" channel. Thank you for having made such a based series that allowed me to create this workshop.

## Features

- No extra installation for users: Participants SSH directly to the host's machine.
- With graphics: Utilizing `sixel`, Arisu images can be displayed on Windows Terminal.
- Game start condition: Prevent user to start the game at the wrong time. Using a simple HTTP server to send start signal (`arisu_start`).
- Automation: Quickly create new users and copy game files with `deploy` and delete users and files with `cleanup`.
- Embed a secret message: After completing the game's objectives, the user can obtain a secret message (each user can have a unique one).

## Commands & Knowledge Covered in the Game

During the Arisu Game, players will practice and learn the following Linux commands and concepts:

- `echo`: Printing messages.
- `touch`: Creating files.
- `mkdir`: Creating directories.
- `rm, rm -r`: Removing files and directories.
- `ls, ls -a`: Listing files and hidden files in directories.
- `cat`: Viewing the contents of files.
- `cp, mv`: Copying or moving files.
- `chmod`: Changing file permissions to make files readable or locked.
- `top`: Listing running processes.
- `ps, kill`: Listing running processes and terminating them by PID or name.
- `find`: Searching for files or directories within the home directory.
- `grep`: Filtering lines of text.
- `nano`: Simple text editor.
- `>`, `>>`: Output redirection, combining file parts or saving command output to files.
- `|`: Piping, combining commands, pipe the output of one command to the input of another.
- **Process and file permissions**: Understanding how processes can lock files and how to unlock them.
- **Hidden files**: Recognizing and manipulating files that start with a dot (`.`).

## Requirements

- Fish shell (I chose fish because it has autosuggestion by default)
- Dependencies: `base64`, `curl`, `ponysay`, `img2sixel`, `dotacat`
- For the users: [terminal that suapports sixel](https://arewesixelyet.com) (like Windows Terminal).

## So you want to try?

1. Ensure the requirements.
2. Clone the repo (or download as zip and extract), then `cd` into it.
3. Run `deploy` script. Usage: `./scripts/deploy <username> <secret_string>`. It is not recommended to try as the current user, since it will mess up your home folder.
4. Login as the new user and run `./arisu` on `~/`.
5. Run `cleanup` script after finish. Usage: `./script/cleanup <username>`.

## Acknowledge

- [Game thâu đêm](https://www.youtube.com/@gamethaudem): Ideas
- [BlueSechi](https://www.youtube.com/@BlueSechi): Arisu artworks
- REC: Gave me the opportunity to yap about Linux nonstop

Thank you all!

## License

This project is licensed under the MIT License.
