public class Ring {
 
    private SortedMap<Long, T> ring = new TreeMap<Long, T>();
    private HashMap<String, T> nodeMap = new HashMap<String, T>();
    private MD5Hash hash = new MD5Hash();
    private vNodeCount;
 
    public Ring(int vnodeCount, Collection pNodes) {
 
        this.vnodeCount = vnodeCount;
 
        for (T pNode : pNodes) {
            addNode(ring, nodeMap, pNode, vnodeCount);
        }
    }
 
    private void addNode(T pNode, int vnodeCount) {
        for (int i = 0; i < vnodeCount; i++) {
            ring.put(hash.hash(pNode.toString() + i), pNode);
        }
    }
 
        public void removeNode(T node, int vnodeCount) {
          for (int i = 0; i < vnodeCount; i++) {
            ring.remove(hash.hash(pNode.toString() + i));
          }
        }
 
    private T getNodeByObjectId(String objectId) {
 
        long hashValue = hash.hash(objectId);
 
        if (!ring.containsKey(hashValue)) {
            SortedMap<Long, T> tailMap = ring.tailMap(hashValue);
            hashValue = tailMap.isEmpty() ? ring.firstKey() : tailMap.firstKey();
        }
 
        return ring.get(hashValue);
    }
 
    private static class MD5Hash {
        MessageDigest instance;
 
        public MD5Hash() {
            try {
                instance = MessageDigest.getInstance("MD5");
            } catch (NoSuchAlgorithmException e) {
            }
        }
 
        long hash(String key) {
            instance.reset();
            instance.update(key.getBytes());
            byte[] digest = instance.digest();
 
            long h = 0;
            for (int i = 0; i < 4; i++) {
                h <<= 8;
                h |= ((int) digest[i]) & 0xFF;
            }
            return h;
        }
    };
};
