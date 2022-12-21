docker stop db library_app auto_test
docker rm db library_app auto_test
docker rmi library_app_app
docker compose up --build
