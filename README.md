
# Install (Unix)

```
cd ~/my/install/directory

git clone https://github.com/xgilbert/tfl-disruption.git

cd tfl-disruption

# make sure your Docker daemon is running
docker build -t tfl-disruption .
```

# Run

```
# start the application
docker run -d -p 5555:5555 -d tfl-disruption
```

# Valid line names

```
bakerloo
central
circle
district
hammersmith-city
jubilee
metropolitan
northern
piccadilly
victoria
waterloo-city
```


# Time split

* Understand task, research, test TFL API : ~ 45min
* dev/ops, Dockerfile, code boilerplate: ~30min
* app boilerplate, models, resources: ~1h30min
* Postman collection and testing: ~30min
* scheduling logic, research, implementation: ~1h
* README and miscellaneous: ~15min


# TODO
* fix task scheduling, context error
* add tests
* add error handling
* add typing + pydantic objects for validation
* add github action
