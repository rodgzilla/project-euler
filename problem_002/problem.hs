fibonacciSeq :: (Num a) => [a]
fibonacciSeq = 0 : 1 : zipWith (+) fibonacciSeq (tail fibonacciSeq)

answer :: Int
answer = sum . filter even . takeWhile (<4000000) $ fibonacciSeq
