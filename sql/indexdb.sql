-- multicolumn index on (s, t) segment node ids for efficient segment lookups
CREATE INDEX IF NOT EXISTS segments_osm_segments_from_osm_segments_to_idx ON segments USING BTREE (osm_segment_from, osm_segment_to);


-- multicolumn index on (key, val) for efficient segment tag lookup
CREATE INDEX IF NOT EXISTS segments_osm_tag_key_osm_tag_val_idx ON segments USING BTREE (osm_tag_key, osm_tag_val);
