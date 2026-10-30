from pathlib import Path
p=Path('app/src/RoomArena.tsx');s=p.read_text(encoding="utf-8");a=s.index('function Face(');b=s.index('export function RoomArena',a);s=s[:a]+s[b:];s=s.replace("import './room-arena.css';","import './room-arena.css';\nimport {PlayingCard as Face} from './PlayingCard';");p.write_text(s,encoding="utf-8")

