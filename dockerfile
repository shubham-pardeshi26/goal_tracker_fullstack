# Use an official Jupyter image as a parent image
FROM jupyter/base-notebook

# Optionally, install additional dependencies or packages
#RUN pip install --no-cache-dir pandas==1.3.3 
#python==3.10 psycopg2==2.9.3 matplotlib 

# Make port 8888 available to the world outside this container
EXPOSE 8888

# Run Jupyter Notebook on container start
CMD ["start-notebook.sh", "--NotebookApp.token='9dfcd4a1-2768-43f2-b079-2d7f6aeb8a18'", "--NotebookApp.password='shubh@10'"]