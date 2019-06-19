gulp installation

update node:
https://nodejs.org/en/

create the json file:
$ npm init

install gulp globally on your computer:
npm install gulp -g
npm install --save-dev gulp ..... new


install gulp locally on this project:
npm install gulp --save-dev

the new gulp method structure is from here:
https://github.com/gulpjs/gulp/blob/master/docs/recipes/running-tasks-in-series.md


https://www.sitepoint.com/how-to-migrate-to-gulp-4/

edit the pathes in gulp.js to match the new project

install the required packages:
browsersync locally:
npm install browser-sync --save-dev

gulp-sass:
npm install gulp-sass --save-dev

i edited the gulpfile: removed runserver function, and edited gulp.watch() on change.

run gulp 