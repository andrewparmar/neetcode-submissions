class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length != t.length) {
            return false
        }

        console.log(s, t)

        const sMap = new Map()
        const tMap = new Map()

        for (let i=0; i < s.length; i++) {
            sMap.set(s[i], (sMap.get(s[i]) ?? 0) + 1)
            tMap.set(t[i], (tMap.get(t[i]) ?? 0) + 1)
        }

        console.log("here")
        console.log(sMap)
        console.log(tMap)

        for (const [key, value] of sMap) {
            console.log("here 2")
            console.log(key)
            if (value !== (tMap.get(key) ?? 0)) {
                return false
            }
        }

        return true
    }
}
