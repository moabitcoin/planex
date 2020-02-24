CREATE TABLE IF NOT EXISTS segments (

  -- the map version e.g. 20191106
  map_version INT NOT NULL,

  -- the segment's parent way id
  osm_way_id BIGINT NOT NULL,

  -- the segment's source node id
  osm_segment_from BIGINT NOT NULL,

  -- the segment's target node id
  osm_segment_to BIGINT NOT NULL,

  -- the segment's tag key e.g. highway in highway=primary
  osm_tag_key VARCHAR(256) NOT NULL,

  -- the segment's tag value e.g. primary in highway=primary
  osm_tag_val VARCHAR(256) NOT NULL,

  -- the timestamp for the segment's parent way creation
  creation_timestamp TIMESTAMP WITH TIME ZONE NOT NULL

);
