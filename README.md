# Extract and merge PDF pages (combine_pdfs)
<a href="https://github.com/FernandoTorresL/combine_pdfs/commits/main" target="_blank">![GitHub last commit](https://img.shields.io/github/last-commit/FernandoTorresL/combine_pdfs)</a>

<a href="https://github.com/FernandoTorresL/combine_pdfs" target="_blank">![GitHub repo size](https://img.shields.io/github/repo-size/FernandoTorresL/combine_pdfs)</a>
## Project: Combining select pages from some PDFs.

Combine all the PDFs on working directory /archivos_pdfs into a single PDF on parent folder

### Technology used

This project was build with the use of:

- Python v3.11.4

## Installation

Create a Python virtual environment

OS X & Linux:

```sh
$ python -m venv ./venv
$ source ./venv/bin/activate
$ pip install --upgrade pip
$ pip3 install -r requirements.txt
(venv) $
```

Windows:
```sh
$ python -m venv venv
$ .\venv\Scripts\activate
$ pip3 install -r requirements.txt
(venv) $
```

Windows 10 with Git bash terminal:
```sh
$ python -m venv venv
$ source ./venv/Scripts/activate
$ pip3 install -r requirements.txt
(venv) $
```

Windows 10 with powershell terminal:
```sh
PS> python -m venv venv
PS> .\.venv\Scripts\Activate.ps1
PS> pip3 install -r requirements.txt
(.venv) PS>
```

> This prompt may vary if you use another shell configuration, like pk10 or git bash

Later, to deactivate the virtual environment
OS X & Linux & Windows:

```sh
(venv) $ deactivate
$
```

## Run the project

Before run this project, be sure this folder exist:

* archivos_pdfs/

Copy some PDF files on this folder

Then, you can execute the program:

```sh
python combine_pdfs.py
```

## Example

```sh
python combine_pdfs.py
```


### Output files

* ./PDF_combinado.pdf, PDF file with the merge document from all the extracted pages

## Contributing to this repo

1. Fork it (<https://github.com/FernandoTorresL/combine_pdfs/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

---

<div align="center">
    <a href="https://fertorresmx.dev/">
      <img height="150em" src="https://raw.githubusercontent.com/FernandoTorresL/FernandoTorresL/main/media/FerTorres-dev1.png">
  </a>
</div>



#### Follow me 
[fertorresmx.dev](https://fertorresmx.dev/)

#### :globe_with_meridians: [Twitter](https://twitter.com/FerTorresMx), [Instagram](https://www.instagram.com/fertorresmx/): @fertorresmx
