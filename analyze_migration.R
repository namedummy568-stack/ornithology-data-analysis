# R script to analyze bird migration data
# Install necessary packages if not already installed
if (!require("ggplot2")) install.packages("ggplot2")
if (!require("dplyr")) install.packages("dplyr")

# Load libraries
library(ggplot2)
library(dplyr)

# Read the migration data
migration_data <- read.csv("migration_data.csv")

# Convert MigrationDate to Date object
migration_data$MigrationDate <- as.Date(migration_data$MigrationDate)

# Basic summary statistics
summary(migration_data)

# Plot migration patterns by species
ggplot(migration_data, aes(x = MigrationDate, y = LocationLat, color = Species)) +
  geom_point() +
  labs(title = "Bird Migration Patterns by Species",
       x = "Migration Date",
       y = "Latitude") +
  theme_minimal()

# Save the plot
ggsave("migration_patterns.png")

# You can add more complex analysis here, e.g.,
# migration_data %>%
#   group_by(Species) %>%
#   summarise(AvgLat = mean(LocationLat), AvgLon = mean(LocationLon))
