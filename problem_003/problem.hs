factorDivisor :: (Integral a) => a -> a -> [a]
factorDivisor x y
  | y > x          = []
  | x `mod` y == 0 = y : factorDivisor (x `div` y) 2
  | otherwise      = factorDivisor x (y + 1)

factorize :: (Integral a) => a -> [a]
factorize x = factorDivisor x 2

answer :: Integer
answer = maximum . factorize $ 600851475143
