# datastreaming-crime-sf

1.- How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

setting maxOffsetsPerTrigger to high values will affect the throughput and latency. 
You can check processedRowsPerSecond and inputRowsPerSecond values that will be affected.

2.- What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

In order to meassure  and test I checked with differents values:

I checked the value of processedRowsPerSecond, maxOffsetsPerTrigger, maxRatePerPartition, parallelism, partitions...

Finally the best result was with these settings:

spark.streaming.kafka.maxRatePerPartition : 10

spark.default.parallelism : 3
