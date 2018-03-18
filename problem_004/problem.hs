isPalindromeString :: String -> Bool
isPalindromeString []  = True
isPalindromeString [x] = True
isPalindromeString s
  | head s == last s = isPalindromeString . init . tail $ s
  | otherwise        = False

answer :: Int
answer = maximum [x * y | x <- [0..999], y <- [0..999], isPalindromeString . show $ x * y]

answer' :: Int
answer' = maximum [x * y | x <- [0..999], y <- [0..999], (reverse . show $ x * y) == (show $ x * y)]

-- Solution from https://wiki.haskell.org/Euler_problems/1_to_10
answer'' :: Int
answer'' = maximum [x | y <- [100..999], z <- [100..999], let x = y * z, let s = show x, s == reverse s]
