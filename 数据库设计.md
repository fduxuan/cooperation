# 移动互联网 project

## cornerstone  后端 api 及数据库字段设计

**@fduxuan**

**Mongodb放光彩** 

### 1 user

#### 1.1 数据库架构

| 字段       | 类型 | 描述                                           |
| ---------- | ---- | ---------------------------------------------- |
| _id        | str  | Mongo 存储生成id                               |
| name       | str  | 姓名                                           |
| collection | List | 收藏夹中的计划 [id1,id2,id3]                   |
| avatar     | url  | false时代表默认图片，true时调用获得avatar的api |
| friends    | list | 好友id，[id1,id2,id3]形式存储                  |



#### 1.2 api设计

| api                     | 类型   | 描述              |
| ----------------------- | ------ | ----------------- |
| /api/user/find          | create | 查找所有的user    |
| /api/user/update        | post   | 更新字段          |
| /api/user/avatar/upload | post   | 上传头像          |
| /api/user/info/<uid>    | get    | 获得对应uid的信息 |
| /api/user/avatar/show   | Get    | 获得对应头像      |



### 2 notification

#### 2.1 数据库架构

| 字段     | 类型 | 描述                                         |
| -------- | ---- | -------------------------------------------- |
| _id      | Str  |                                              |
| from_who | Str  | 发送者uid                                    |
| to       | Str  | 接收者uid                                    |
| tag      | str  | 暂定 comment/like/message （评论/点赞/私信） |
| is_read  | Bool | False->未读， true->已读                     |
| detail   | str  | 具体消息内容                                 |
| plan_id  | str  | 相关的plan id                                |



#### 2.2 api设计

针对消息的具体操作都需要判断owner权限

| api                             | 类型 | 描述             |
| ------------------------------- | ---- | ---------------- |
| /api/notification/send/to/<uid> | Post | 发送             |
| /api/notification/<nid>/read    | Get  | 已读             |
| /api/notification/<nid>/unread  | Get  | 标为未读         |
| /api/notification/show/<nid>    | Get  | 获得消息详细内容 |
| /api/notification/delete/<nid>  | Get  | 删除消息         |



### 3 plan

#### 3.1 数据库架构

| 字段    | 类型 | 描述                                                         |
| ------- | ---- | ------------------------------------------------------------ |
| _id     | Str  |                                                              |
| node    | List | [{"desc": "xxx", "detail":["xxx",'xxx']},{},{}]  list中每日plan，根据设置的时间可以自动扩充复制 |
| Owner   | Str  | 创建者id                                                     |
| time    | int  | 持续时间的天数                                               |
| id      | list | [uid1,uid2,uid3….].   用户可以用 $in判断是否存在与这个里面   |
| Comment | List | [nid1,nid2,nid3….]   暂定comment 不可删除（notification删除的是消息而不是comment本身） |



#### 3.2 api设计

| api                     | 类型 | 描述                                        |
| ----------------------- | ---- | ------------------------------------------- |
| /api/plan/create        | Post | 创建属于自己的plan                          |
| /api/plan/like/<pid>    | Get  | 点赞                                        |
| /api/plan/comment/<pid> | Post | 评论                                        |
| /api/plan/collect/<pid> | Get  | 收藏                                        |
| /api/plan/use/<pid>     | Post | 使用该计划，创建session，并指定好友一同进行 |
| /api/plan/show/<pid>    | Get  | 获得详细信息                                |



### 4 session

正在进行的plan

#### 4.1 数据库架构

| 字段        | 类型 | 描述                   |
| ----------- | ---- | ---------------------- |
| _id         | Str  |                        |
| plan_id     | Str  |                        |
| Now_time    | Int  | 进行到第几天           |
| Participant | list | [uid1,uid2] 参与者     |
| time        | Int  | 总时间                 |
| goals       | list | [int, int]  参与者得分 |
| node        |      |                        |



#### 4.2 api设计

| api                     | 类型 | 描述                                   |
| ----------------------- | ---- | -------------------------------------- |
| /api/session/show/<sid> | Get  |                                        |
| /api/session/done       | post | post 字段有 当前时间，对手id，返回得分 |
|                         |      |                                        |

