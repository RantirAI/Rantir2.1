# Rantir

## Steps to run dev env locally via docker

### First Option

- Clone the repo 

   - git clone -b test git@github.com:RantirAI/Rantir2.1.git

- cd into Rantir2.1
 
  - cd Rantir2.1

- create .nuxt and .nuxt-storybook in web-frontend directory and change permission to read and write by everyone

  -  mkdir web-frontend/.nuxt && chmod -R 777 web-frontend/.nuxt

  -  mkdir web-frontend/.nuxt-storybook && chmod -R 777 web-frontend/.nuxt-storybook

- change permission for backend email compiler for read and write in backend directory

  - chmod -R 777 backend/email_compiler

  - chmod -R 777  backend/src/baserow/core/templates/baserow/core

- Build the images using this command

  - ./dev.sh no_e2e ignore_ownership --build


 
### Watch the Video
[Watch the video](assets/video.webm)

### OPTION 2
- Clone the repo

   - git clone -b test git@github.com:RantirAI/Rantir2.1.git

- cd into Rantir2.1

  - cd Rantir2.1

- Copy .env.dev.example to .env

  - cp .env.dev.example .env

- Replace the values of uid and guid in .env as 9999

- create .nuxt in web-frontend directory and change permission to read and write by everyone

  - mkdir web-frontend/.nuxt && chmod -R 777 web-frontend/.nuxt

- Run the following command to build and run the only required containers for the app

  - docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build web-frontend
