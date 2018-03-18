isPalindromeString :: String -> Bool
isPalindromeString []  = True
isPalindromeString [x] = True
isPalindromeString s
  | head s == last s = isPalindromeString . init . tail $ s
  | otherwise        = False

answer :: Int
answer = maximum [x * y | x <- [999,998..0], y <- [999,998..0], isPalindromeString . show $ x * y]
