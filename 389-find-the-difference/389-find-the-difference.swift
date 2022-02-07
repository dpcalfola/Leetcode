class Solution {
	func findTheDifference(_ s: String, _ t: String) -> Character {

		let chaS: [Character] = s.map{ $0 }.sorted()
		let chaT: [Character] = t.map{ $0 }.sorted()

		for i in 0..<chaS.count{
			if chaS[i] != chaT[i]{
				return chaT[i]
			}
		}

		return chaT[chaT.count-1]
	}
}
