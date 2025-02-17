# Rantir

## Steps to run dev env locally via docker

- Clone the repo 

   - git clone -b test git@github.com:RantirAI/Rantir2.1.git

- cd into Rantir2.1
 
  - cd Rantir2.1

- create .nuxt and .nuxt  .nuxt-storybook in web-frontend directory and change permission to read and write by everyone

  -  mkdir web-frontend/.nuxt && chmod -R 777 web-frontend/.nuxt

  -  mkdir web-frontend/.nuxt-storybook && chmod -R 777 web-frontend/.nuxt-storybook

- change permission for backend email compiler for read and write in backend directory

  - chmod -R 777 backend/email_compiler

- Replace the values of group id ( gid) and userid (uid) in .env.dev.example  by getting your userid and groupid 

- Build the images using this command

  - ./dev.sh no_e2e ignore_ownership --build


 
## Watch the Video
[Watch the video](assets/video.webm)

