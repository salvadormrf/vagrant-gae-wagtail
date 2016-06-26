Vagrant GAE
----------------------------------------

Vagrant development box to run Google AppEngine.

Documentation
----------------------------------------

### Install Vagrant & VirtualBox (OSX Instructions)
    brew cask install virtualbox
    brew cask install vagrant
  
### Run development box
    vagrant up  
    vagrant ssh  

    cd project
    make run

### Application access

Access **website** from:
- [http://wagtailgaedemo.dev:8080/](http://wagtailgaedemo.dev:8080/) 
- [http://wagtailgaedemo.dev:8000/](http://wagtailgaedemo.dev:8000/) (GAE)
