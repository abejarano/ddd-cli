# ddd-cli


### instar
1-. Clona el script Python
```
git clone https://github.com/abejarano/ddd-cli
```

2-. Mueve el script Python a /usr/local/bin
```
sudo mv ddd-cli.py /usr/local/bin/
```
3-. Añade export PATH="/usr/local/bin:$PATH" al archivo ~/.zshrc si no está presente
```
if ! grep -q '/usr/local/bin' ~/.zshrc; then
    echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
    echo 'PATH updated in ~/.zshrc'
fi
```
4-. Actualiza el entorno actual

source ~/.zshrc

```
