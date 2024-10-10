# Polygon Algorithms

## Prerequisites
- **Python 2.7**
- **Python 3**
- **Linux environment** (preferred)
- **Docker** (Desktop or CLI)

> **Note:** It is possible to run the code without Docker, but using Docker resolves major version conflicts and inconsistencies. Hence, it is strongly recommended.

## How to Run

1. Ensure you have the prerequisites satisfied.

2. Pull the Docker image and spawn a container with the following command:
   ```bash
   docker run -it sourabhkulkarni14/myimage:latest
   ```
   > **Note:** Containers are used here to ensure no version conflicts arise within Python 2.7 and Python 3 libraries. You can also build the image yourself using the provided Dockerfile.

3. Clone the repository with the algorithm implementations:
   ```bash
   git clone https://github.com/ggarvit21/Polygon-Algorithm
   ```

4. Change directory to the cloned repository:
   ```bash
   cd Polygon-Algorithm/
   ```

5. Execute `main.py` with Python 2.7 and specify the desired number of vertices:
   ```bash
   python2 main.py <No_of_Vertices>
   ```

   > **Note:** If run through Docker, images will be saved. If run outside of Docker, Python images will pop up.
