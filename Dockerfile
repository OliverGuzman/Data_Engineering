# Image of mongoDB
FROM mongo:latest

# Install Python
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Create and set Python virtual environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Install pymongo
RUN pip3 install pymongo
RUN pip3 install pandas

# Set working directory
WORKDIR /project_data_engineering

# Copy Python scripts
COPY load_data.py ./

# Copy data files
COPY data.csv ./

# Create script to start MongoDB and run Python script
RUN echo '#!/bin/bash\n\
# Start MongoDB service\n\
mongod --fork --logpath /var/log/mongodb.log\n\
\n\
# Wait for MongoDB to start up properly\n\
sleep 5\n\
\n\
# Run the Python data import script\n\
python3 load_data.py\n\
sleep 100\n\
' > /startup.sh

# Make script executable
RUN chmod +x /startup.sh

# Set environment variables
ENV MONGO_INITDB_DATABASE=mongodb
ENV PYTHONUNBUFFERED=1

# Expose MongoDB port
EXPOSE 27017

# Run the script when container starts
CMD ["/startup.sh"]
