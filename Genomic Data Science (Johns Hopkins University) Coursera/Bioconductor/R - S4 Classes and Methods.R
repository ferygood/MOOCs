#R -S4 Classes and Methods
biocLite(c("ALL","GenomicRanges"))

#S4 system in R is a system for object oriented programming
library(ALL)
data(ALL)
ALL
class(ALL)
isS4(ALL)

#Constructors and getting help
#finding help
?"ExpressionSet-class"
class?ExpressionSet

xx <- list(a=1:3)
ExpressionSet()
?ExpressionSet
new("ExpressionSet")

#Slots and accessor functions
getClass("ExpressionSet")
ALL@annotation
slot(ALL, "annotation")
annotation(ALL)

#Outdated S4 classes
new_object <- updateObject(old_object)
object <- updateObject(object)
validObject(ALL)

#S4 Methods
mimicMethod <- function(x) {
  if (is(x, "matrix"))
    method1(x)
  if (is(x, "data.frame"))
    method2(x)
  if (is(x, "IRanges"))
    method3(x)
}

as.data.frame
showMethods("as.data.frame")
getMethod("as.data.frame","DataFrame")
base::as.data.frame

#Example where two different methods of the generic have different arguments
getMethod("findOverlaps", signature(query = "Ranges", subject = "Ranges"))
getMethod("findOverlaps", signature(query = "GenomicRanges", subject = "GenomicRanges"))

#R version 3.2.1
#ALL_1.10.0
#S4Vectors_0.6.3
