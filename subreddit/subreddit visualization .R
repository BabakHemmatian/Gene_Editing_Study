install.packages("tidyverse")
library("ggplot2")
install.packages("plotly")
library("plotly")

mydata <- read.csv("subreddit_contribtutions_for_visuals.csv")
mydata <- as.data.frame(subreddit_contributions_for_visuals)
class(mydata)

relevant_topics <- select(mydata, V5, V9, V12, V13, V15, V16, V17, V18, V19, V24, V26, V28, V41, V45, V48, V49, V51)
class(relevant_topics)
row.names(relevant_topics) <- c("AskReddit", "science", "Futurology", "askscience", "worldnews", "todayilearned", "explainlikeimfive", "changemyview","biology", "news")
transposed <- t(relevant_topics)
transposed <- as.data.frame(transposed)
class(transposed)
print(transposed)

print(transposed["AskReddit"])
x_values <- c()
for (i in transposed["AskReddit"]){
  append(x_values, i)
}
class(transposed)
print(x_values)

topic_names <- c("Unintended \n Consequences", "Morality", "Future Genetic \n Changes", "Genetic Treatments \nto Disease", "Biological Function \n of Crispr", "Cures", "Should We Use \n Genetic Engineering", "Stem Therapies", "Children with \n Genetic Mutation", "V22", "Gene Therapy \n Development", "V27", "Postulating on \n Crispr", "Changing Human \n Genetics", "Future with GE", "Complications with \n GE", "Looking Towards\n the Future")

barplot(as.matrix(transposed$AskReddit), main = "AskReddit", xlab = "Topics", ylab = "contribution",names.arg = topic_names, beside = TRUE, las = 2, cex.names = .5)
barplot(as.matrix(transposed$science), main = "science", xlab = "Topics", ylab = "contribution",names.arg = topic_names , beside = TRUE, las = 2, cex.names = .5)
barplot(as.matrix(transposed$Futurology), main = "Futurology", xlab = "Topics", ylab = "contribution",names.arg = topic_names , beside = TRUE, las = 2, cex.names = .5)
barplot(as.matrix(transposed$askscience), main = "askscience", xlab = "Topics", ylab = "contribution",names.arg = topic_names , beside = TRUE, las = 2, cex.names = .5)
barplot(as.matrix(transposed$worldnews), main = "worldnews", xlab = "Topics", ylab = "contribution",names.arg = topic_names , beside = TRUE, las = 2, cex.names = .5)
barplot(as.matrix(transposed$todayilearned), main = "todayilearned", xlab = "Topics", ylab = "contribution",names.arg = topic_names , beside = TRUE, las = 2, cex.names = .5)
barplot(as.matrix(transposed$explainlikeimfive), main = "explainlikeimfive", xlab = "Topics", ylab = "contribution",names.arg = topic_names , beside = TRUE, las = 2, cex.names = .5)
barplot(as.matrix(transposed$changemyview), main = "changemyview", xlab = "Topics", ylab = "contribution",names.arg = topic_names , beside = TRUE, las = 2, cex.names = .5)
barplot(as.matrix(transposed$biology), main = "biology", xlab = "Topics", ylab = "contribution",names.arg = topic_names , beside = TRUE, las = 2, cex.names = .5)
barplot(as.matrix(transposed$news), main = "news", xlab = "Topics", ylab = "contribution",names.arg = topic_names , beside = TRUE, las = 2, cex.names = .5)

