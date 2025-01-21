FROM node:18-alpine

WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm ci

# Copy application code
COPY . .

# Start development server with host set for Docker
CMD ["npm", "run", "dev", "--", "--host"]