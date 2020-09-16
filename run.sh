docker build . -t bms -f Dockerfile
docker run --rm -p 8000:8000 -v $(pwd):/code -ti bms