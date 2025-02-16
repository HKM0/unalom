module Karacsonyfa where


--funckprog 5. HF adta az ötletet.

sor :: Integral i => i -> i -> String
sor szelesseg a = replicate (fromIntegral (szelesseg - a))' ' ++ replicate (fromIntegral(2 * a - 1)) '#'
fa :: Integral i => i -> String
fa 0 = ""
fa a = init (concatMap (\x -> sor a x ++ "\n")[1..a]) 
torzs :: Integral i => i -> String
torzs a | a <= 3 = replicate (fromIntegral (a - 1)) ' ' ++ "|"
torzs a = replicate (fromIntegral (a - 2)) ' ' ++ "|||"
teljesfa :: Integral i => i -> String
teljesfa a = fa a ++ "\n" ++ torzs a

--putStrLn (teljesfa 10)
