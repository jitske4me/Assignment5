##Koeleman Individual Assignment 5
library('tidyverse')
library('maps')
library('mapdata')

iraq <- read.csv('preprocessed_conflict_data_Iraq.csv')
iraq.IS <- read.csv('preprocessed_conflict_data_Iraq_IS.csv')

# ## Make a data.frame with IS deaths from 2005-2010 by Iraqi Government
# iraq.IS.0515 <- iraq.IS %>%
#   filter(year >= 2005) %>%
#   droplevels()

## Make a scatterplot
ggplot(data = iraq) + 
  geom_point(mapping = aes(x = side_b, y = side_a, size = deaths_b))+
  theme(axis.text.x = element_text(angle=270)) #, colour = deaths_a+deaths_b ))

## Make a data.frame with IS deaths from 2005-2010 by Iraqi Government
iraq.IS.0510 <- iraq.IS %>%
  filter(year >= 2005 & year < 2010) %>%
  filter(side_b == 'IS' & side_a == 'Government of Iraq')%>%
  droplevels()

## Make a data.frame with IS deaths from 2010-2015 by Iraqi Government
iraq.IS.1015 <- iraq.IS %>%
  filter(year >= 2010 & year <= 2015)%>%
  filter(side_b == 'IS'& side_a == 'Government of Iraq')%>%
  droplevels()
  
## Plot the data points for year 2005-2010
## IS people that died 
ggplot() +
  geom_polygon(data = map_data('world','Iraq'), mapping = aes(x=long, y=lat, group=group), fill = "grey", color = "black")+ 
  geom_point(data = iraq.IS.0510, mapping = aes(x = longitude, y = latitude, colour = side_a, size = deaths_b))

## Plot the data points for year 2010-2015
## IS people that died 
ggplot() +
  geom_polygon(data = map_data('world','Iraq'), mapping = aes(x=long, y=lat, group=group), fill = "grey", color = "black")+ 
  geom_point(data = iraq.IS.1015, mapping = aes(x = longitude, y = latitude, colour = side_a, size = deaths_b))
