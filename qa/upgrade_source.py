from pathlib import Path
p=Path('app/src/main.tsx');s=p.read_text(encoding='utf-8-sig')
s=s.replace('useNavigate, useParams','useNavigate').replace(', Check, UserPlus','')
s=s.replace("import './styles.css';","import './styles.css';\nimport {Button, UIKit} from './Button';\nimport {RoomArena} from './RoomArena';")
for name in ['useStore','person','Avatar','Modal']:
 s=s.replace('function '+name+'(', 'export function '+name+'(')
s=s.replace('const people:','export const people:')
a=s.index('function RoomPage()');b=s.index('function LeaderboardPage()',a);s=s[:a]+s[b:]
s=s.replace('<AppShell><RoomPage/></AppShell>','<RoomArena/>')
s=s.replace('<Routes>','<Routes><Route path="/ui-kit" element={<UIKit/>}/>')
s=s.replace('<button','<Button').replace('</button>','</Button>')
s=s.replace('<Button className="primary" disabled={!valid}>','<Button type="submit" variant="primary" className="primary" disabled={!valid}>')
s=s.replace('<Button className="primary">Tham gia','<Button type="submit" variant="primary" className="primary">Tham gia')
s=s.replace('<Button className="primary" disabled={name.trim().length<2}>','<Button type="submit" variant="primary" className="primary" disabled={name.trim().length<2}>')
s=s.replace('<Button className="primary" aria-label="Gửi">','<Button type="submit" variant="primary" className="primary" aria-label="Gửi">')
p.write_text(s,encoding='utf-8')
