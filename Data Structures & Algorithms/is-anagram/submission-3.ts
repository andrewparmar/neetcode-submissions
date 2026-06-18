class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length !== t.length) {
            return false
        }

        const sMap: Map<string, number> = new Map()
        const tMap: Map<string, number> = new Map()

        // for (let i=0; i < s.length; i++) {
        //     sMap.set(s[i], (sMap.get(s[i]) ?? 0) + 1)
        //     tMap.set(t[i], (tMap.get(t[i]) ?? 0) + 1)
        // }
        // for (const [key, val] of sMap) {
        //     if (tMap.get(key) !== val) return false
        // }
        // return true


        const mapping: Map<string, number> = new Map()
        for (let i=0; i < s.length; i++) {
            mapping.set(s[i], (mapping.get(s[i]) ?? 0) + 1)
            mapping.set(t[i], (mapping.get(t[i]) ?? 0) - 1)
        }
        for (const ch of t) {
            if (mapping.get(ch) === 0) {
                mapping.delete(ch)
            }
        }
        return mapping.size === 0
    }
}
