# Surprise Practical Work

A fast-made practical work.

## Technologies

 - Flask
 - Docker

## Set-Up

To deploy this project you will need an updated version of Python.
First, we will create a virtual enviroment. You can do it with
```bash
  python3 -m venv venv
```
Now, we need to activate the virtual enviroment.
On linux, just type
```bash
  source venv/bin/activate
```
on Windows,
```bash
   venv/Scripts/activate
```
Once activated, we need to install Flask and other libraries:

```bash
  pip install -r requirements.txt
```
After, we have to run on terminal the following sentence, in order to build the docker image.

```bash
  sudo docker-compose build
```
Lastly, we must run the container to see the project from our localhost.

```bash
  sudo docker-compose up -d
```

and access it through typing [localhost:5000](http://localhost:5005/) in your browser


## Author

- [@Nazareno Bucciarelli](https://github.com/nazabucciarelli)
