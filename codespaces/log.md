# creation logs


## Sat  2 Dec 05:32:25 GMT 2023
```
=================================================================================
2023-12-02 05:25:30.421Z: Configuration starting...
2023-12-02 05:25:30.469Z: Cloning...
2023-12-02 05:25:30.517Z: $ git -C "/var/lib/docker/codespacemount/workspace" clone --branch "49-codespaces" --depth 1 https://github.com/mxochicale/code "/var/lib/docker/codespacemount/workspace/code"
2023-12-02 05:25:30.533Z: Cloning into '/var/lib/docker/codespacemount/workspace/code'...
2023-12-02 05:25:33.881Z: git process exited with exit code 0
2023-12-02 05:25:33.891Z: $ git -C "/var/lib/docker/codespacemount/workspace/code" config --local remote.origin.fetch +refs/heads/*:refs/remotes/origin/*
2023-12-02 05:25:33.897Z: git process exited with exit code 0

=================================================================================
2023-12-02 05:25:34.616Z: Creating container...
2023-12-02 05:25:34.656Z: $ devcontainer up --id-label Type=codespaces --workspace-folder /var/lib/docker/codespacemount/workspace/code --mount type=bind,source=/.codespaces/agent/mount/cache,target=/vscode --user-data-folder /var/lib/docker/codespacemount/.persistedshare --container-data-folder .vscode-remote/data/Machine --container-system-data-folder /var/vscode-remote --log-level trace --log-format json --update-remote-user-uid-default never --mount-workspace-git-root false --omit-config-remote-env-from-metadata --skip-non-blocking-commands --skip-post-create --config "/var/lib/docker/codespacemount/workspace/code/.devcontainer/devcontainer.json" --override-config /root/.codespaces/shared/merged_devcontainer.json --default-user-env-probe loginInteractiveShell --container-session-data-folder /workspaces/.codespaces/.persistedshare/devcontainers-cli/cache --secrets-file /root/.codespaces/shared/user-secrets-envs.json
2023-12-02 05:25:34.832Z: @devcontainers/cli 0.52.1. Node.js v18.17.1. linux 6.2.0-1016-azure x64.
2023-12-02 05:25:35.292Z: $ docker buildx build --load --build-arg BUILDKIT_INLINE_CACHE=1 -f /tmp/devcontainercli-root/container-features/0.52.1-1701494735276/Dockerfile-with-features -t vsc-code-ebc7ff1bb830c9ab527f890f7f31279e8e4979e92a94006398168157f6921606 --target dev_containers_target_stage --build-arg _DEV_CONTAINERS_BASE_IMAGE=dev_container_auto_added_stage_label /var/lib/docker/codespacemount/workspace/code
2023-12-02 05:25:35.826Z: #0 building with "default" instance using docker driver

#1 [internal] load .dockerignore
2023-12-02 05:25:35.931Z: #1 transferring context:
2023-12-02 05:25:36.062Z: #1 transferring context: 2B done
#1 DONE 0.3s

2023-12-02 05:25:36.070Z: #2 [internal] load build definition from Dockerfile-with-features
#2 transferring dockerfile: 2.48kB done
2023-12-02 05:25:36.213Z: #2 DONE 0.4s

2023-12-02 05:25:36.217Z: #3 [internal] load metadata for mcr.microsoft.com/devcontainers/miniconda:0-3
2023-12-02 05:25:36.617Z: #3 DONE 0.5s2023-12-02 05:25:36.630Z: 
2023-12-02 05:25:36.772Z: 
#4 [dev_container_auto_added_stage_label 1/3] FROM mcr.microsoft.com/devcontainers/miniconda:0-3@sha256:533777e6c0c2310801735cdde71f4f441cf66b628c411ff97e20752b1d6cc86d
#4 resolve mcr.microsoft.com/devcontainers/miniconda:0-3@sha256:533777e6c0c2310801735cdde71f4f441cf66b628c411ff97e20752b1d6cc86d 0.1s done
2023-12-02 05:25:36.936Z: #4 sha256:533777e6c0c2310801735cdde71f4f441cf66b628c411ff97e20752b1d6cc86d 1.61kB / 1.61kB done
#4 sha256:fbdfa74a59754288e14a6690f1d9a2498467cc83c939a7bcdb65d71f23596b5f 4.47kB / 4.47kB done
2023-12-02 05:25:36.944Z: #4 sha256:c0d89f1c49a26e118bca52d16564d4ca0c851a7616eccfbd3f35a61e759786a6 24.54kB / 24.54kB done
2023-12-02 05:25:37.063Z: #4 ...

#5 [internal] load build context
#5 transferring context: 589B done
#5 DONE 0.2s

#4 [dev_container_auto_added_stage_label 1/3] FROM mcr.microsoft.com/devcontainers/miniconda:0-3@sha256:533777e6c0c2310801735cdde71f4f441cf66b628c411ff97e20752b1d6cc86d
2023-12-02 05:25:37.068Z: #4 sha256:5c1459d3ab8b5e46ac1a0a00134fe2f7b693474eb6d75ace97ecbe811a6f5b0e 0B / 15.76MB 0.2s
#4 sha256:ddf874abf16cc990e0fd75a154a34ca0a03ee310ad895a18fb62ae15bf4171fb 8.39MB / 55.06MB 0.2s
#4 sha256:9a11a33b016bcaf1d0bd4a0857c13c9dc9486d5eb19d808d5c237d0cb271b99a 0B / 406B 0.2s
2023-12-02 05:25:37.164Z: #4 sha256:5c1459d3ab8b5e46ac1a0a00134fe2f7b693474eb6d75ace97ecbe811a6f5b0e 3.15MB / 15.76MB 0.3s
#4 sha256:ddf874abf16cc990e0fd75a154a34ca0a03ee310ad895a18fb62ae15bf4171fb 17.83MB / 55.06MB 0.3s
#4 sha256:9a11a33b016bcaf1d0bd4a0857c13c9dc9486d5eb19d808d5c237d0cb271b99a 406B / 406B 0.3s done
#4 sha256:b837e19a13f10adaa26316a877e8a3b54df5cf7543914009d2ee02b41d64378f 0B / 134B 0.3s
2023-12-02 05:25:37.339Z: #4 sha256:5c1459d3ab8b5e46ac1a0a00134fe2f7b693474eb6d75ace97ecbe811a6f5b0e 13.63MB / 15.76MB 0.4s2023-12-02 05:25:37.371Z: 
#4 sha256:ddf874abf16cc990e0fd75a154a34ca0a03ee310ad895a18fb62ae15bf4171fb 25.17MB / 55.06MB 0.4s
#4 sha256:b837e19a13f10adaa26316a877e8a3b54df5cf7543914009d2ee02b41d64378f 134B / 134B 0.4s done
2023-12-02 05:25:37.465Z: #4 sha256:5c1459d3ab8b5e46ac1a0a00134fe2f7b693474eb6d75ace97ecbe811a6f5b0e 15.76MB / 15.76MB 0.5s
#4 sha256:ddf874abf16cc990e0fd75a154a34ca0a03ee310ad895a18fb62ae15bf4171fb 30.41MB / 55.06MB 0.5s
2023-12-02 05:25:37.469Z: #4 sha256:be88e9b1429e6abe1be4803e5f9560c271a407bd97941c12e81be9025abdab2d 223B / 223B 0.5s
2023-12-02 05:25:37.615Z: #4 sha256:5c1459d3ab8b5e46ac1a0a00134fe2f7b693474eb6d75ace97ecbe811a6f5b0e 15.76MB / 15.76MB 0.6s done
#4 sha256:ddf874abf16cc990e0fd75a154a34ca0a03ee310ad895a18fb62ae15bf4171fb 51.38MB / 55.06MB 0.7s
2023-12-02 05:25:37.623Z: #4 sha256:be88e9b1429e6abe1be4803e5f9560c271a407bd97941c12e81be9025abdab2d 223B / 223B 0.6s done
#4 sha256:469dc137be941824529e4f076cc2bbc129231c822962ad32580a4e2cd452253c 0B / 232B 0.7s
#4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 0B / 108.29MB 0.7s
2023-12-02 05:25:37.792Z: #4 sha256:ddf874abf16cc990e0fd75a154a34ca0a03ee310ad895a18fb62ae15bf4171fb 55.06MB / 55.06MB 0.9s2023-12-02 05:25:37.799Z: 
2023-12-02 05:25:37.874Z: #4 sha256:469dc137be941824529e4f076cc2bbc129231c822962ad32580a4e2cd452253c 232B / 232B 0.7s done
#4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 7.56MB / 108.29MB 0.9s
#4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 0B / 155.98MB 0.9s
2023-12-02 05:25:37.899Z: #4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 16.78MB / 108.29MB 1.1s
#4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 11.53MB / 155.98MB 1.1s2023-12-02 05:25:37.911Z: 
2023-12-02 05:25:38.037Z: #4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 24.12MB / 108.29MB 1.1s2023-12-02 05:25:38.049Z: 
2023-12-02 05:25:38.171Z: #4 sha256:ddf874abf16cc990e0fd75a154a34ca0a03ee310ad895a18fb62ae15bf4171fb 55.06MB / 55.06MB 1.2s done
#4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 40.89MB / 108.29MB 1.3s
2023-12-02 05:25:38.204Z: #4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 37.75MB / 155.98MB 1.3s
#4 sha256:f7abe09e5d5e4def17605244e9a4f2e8203b1d8d544fa30396d5ec42e6c47bf9 0B / 638B 1.3s
2023-12-02 05:25:38.281Z: #4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 51.18MB / 108.29MB 1.4s
#4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 47.19MB / 155.98MB 1.4s2023-12-02 05:25:38.287Z: 
#4 sha256:f7abe09e5d5e4def17605244e9a4f2e8203b1d8d544fa30396d5ec42e6c47bf9 638B / 638B 1.4s done
#4 extracting sha256:ddf874abf16cc990e0fd75a154a34ca0a03ee310ad895a18fb62ae15bf4171fb
2023-12-02 05:25:38.432Z: #4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 56.95MB / 108.29MB 1.5s
#4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 0B / 118.40MB 1.5s2023-12-02 05:25:38.440Z: 
2023-12-02 05:25:38.602Z: #4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 63.96MB / 108.29MB 1.6s2023-12-02 05:25:38.611Z: 
2023-12-02 05:25:38.635Z: #4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 60.82MB / 155.98MB 1.6s2023-12-02 05:25:38.655Z: 
2023-12-02 05:25:38.744Z: #4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 8.39MB / 118.40MB 1.8s2023-12-02 05:25:38.771Z: 
2023-12-02 05:25:39.036Z: #4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 78.39MB / 108.29MB 2.1s2023-12-02 05:25:39.045Z: 
2023-12-02 05:25:39.056Z: #4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 73.48MB / 155.98MB 2.1s2023-12-02 05:25:39.068Z: 
2023-12-02 05:25:39.073Z: #4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 14.68MB / 118.40MB 2.1s2023-12-02 05:25:39.078Z: 
2023-12-02 05:25:39.185Z: #4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 94.37MB / 108.29MB 2.3s2023-12-02 05:25:39.191Z: 
2023-12-02 05:25:39.194Z: #4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 86.70MB / 155.98MB 2.3s
#4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 25.17MB / 118.40MB 2.3s2023-12-02 05:25:39.200Z: 
2023-12-02 05:25:39.315Z: #4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 101.12MB / 108.29MB 2.4s
#4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 31.46MB / 118.40MB 2.4s
2023-12-02 05:25:39.457Z: #4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 108.00MB / 108.29MB 2.5s
#4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 100.66MB / 155.98MB 2.5s
#4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 37.75MB / 118.40MB 2.5s
2023-12-02 05:25:39.581Z: #4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 114.65MB / 155.98MB 2.7s
#4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 48.23MB / 118.40MB 2.7s
2023-12-02 05:25:39.860Z: #4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 127.93MB / 155.98MB 2.9s2023-12-02 05:25:39.898Z: 
2023-12-02 05:25:39.915Z: #4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 57.67MB / 118.40MB 2.9s2023-12-02 05:25:39.926Z: 
2023-12-02 05:25:39.983Z: #4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 65.01MB / 118.40MB 3.0s
2023-12-02 05:25:40.114Z: #4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 108.29MB / 108.29MB 3.2s done
#4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 146.90MB / 155.98MB 3.2s
#4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 78.64MB / 118.40MB 3.2s
2023-12-02 05:25:40.266Z: #4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 155.98MB / 155.98MB 3.3s2023-12-02 05:25:40.283Z: 
#4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 85.98MB / 118.40MB 3.3s
#4 sha256:857523023f3af2b5bd1a8e05e269fa461162a454beb866f2e32551c7356fd0b8 122B / 122B 3.3s done
2023-12-02 05:25:40.373Z: #4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 96.47MB / 118.40MB 3.5s
#4 sha256:af0f8691d92b92416b19654d847770431abe5077d51bd1f815dcdf834804ff22 605B / 605B 3.5s
2023-12-02 05:25:40.664Z: #4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 116.39MB / 118.40MB 3.8s
2023-12-02 05:25:40.816Z: #4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 155.98MB / 155.98MB 3.8s done
#4 sha256:af0f8691d92b92416b19654d847770431abe5077d51bd1f815dcdf834804ff22 605B / 605B 3.9s done
#4 sha256:a5f5243ec26f765b90acd2506eb615faaed46a306c1f5a1804b434b72cc8435c 0B / 35.86MB 3.9s
2023-12-02 05:25:40.963Z: #4 sha256:a5f5243ec26f765b90acd2506eb615faaed46a306c1f5a1804b434b72cc8435c 9.68MB / 35.86MB 4.1s
2023-12-02 05:25:41.120Z: #4 sha256:a5f5243ec26f765b90acd2506eb615faaed46a306c1f5a1804b434b72cc8435c 16.08MB / 35.86MB 4.2s
2023-12-02 05:25:41.251Z: #4 sha256:a5f5243ec26f765b90acd2506eb615faaed46a306c1f5a1804b434b72cc8435c 23.19MB / 35.86MB 4.3s
2023-12-02 05:25:41.350Z: #4 sha256:a5f5243ec26f765b90acd2506eb615faaed46a306c1f5a1804b434b72cc8435c 29.73MB / 35.86MB 4.4s
2023-12-02 05:25:41.452Z: #4 sha256:a5f5243ec26f765b90acd2506eb615faaed46a306c1f5a1804b434b72cc8435c 35.86MB / 35.86MB 4.5s
2023-12-02 05:25:41.563Z: #4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 118.40MB / 118.40MB 4.6s done
#4 sha256:1fbeb5db8b38e923a081350f3d836fb3b593c83f50566f296561558143d16f11 130B / 130B 4.7s
2023-12-02 05:25:41.864Z: #4 sha256:a5f5243ec26f765b90acd2506eb615faaed46a306c1f5a1804b434b72cc8435c 35.86MB / 35.86MB 4.9s done2023-12-02 05:25:41.865Z: 
#4 sha256:1fbeb5db8b38e923a081350f3d836fb3b593c83f50566f296561558143d16f11 130B / 130B 5.0s done
#4 sha256:f130883feb0eb350abe241dc9409fb73dd51704ad3ae92b536563eb149b33346 412B / 412B 5.0s
#4 sha256:af7055f83fa381583c03a343562a0c407db2d45bd28d4e323034c8f06d2f2a2e 0B / 289B 5.0s
2023-12-02 05:25:41.964Z: #4 sha256:f130883feb0eb350abe241dc9409fb73dd51704ad3ae92b536563eb149b33346 412B / 412B 5.1s done
#4 sha256:4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1 32B / 32B 5.1s
#4 sha256:7ec8d5cae060f1455aec6189e1de7858b03dc8073c461a5e717fed7c336d28b8 0B / 225B 5.1s
2023-12-02 05:25:42.102Z: #4 sha256:af7055f83fa381583c03a343562a0c407db2d45bd28d4e323034c8f06d2f2a2e 289B / 289B 5.1s done2023-12-02 05:25:42.106Z: 
#4 sha256:4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1 32B / 32B 5.2s done
#4 sha256:7ec8d5cae060f1455aec6189e1de7858b03dc8073c461a5e717fed7c336d28b8 225B / 225B 5.2s
#4 sha256:59d5b1cf8ef097657e4c2157443131e4e14997efb3a0042f4f7bd43bc4c8d566 0B / 60.61MB 5.2s
2023-12-02 05:25:42.204Z: #4 sha256:7ec8d5cae060f1455aec6189e1de7858b03dc8073c461a5e717fed7c336d28b8 225B / 225B 5.3s done
#4 sha256:9da9948bb761fa37083d3c9a1fd71e7e3a93951fb0786bf3cab014068fbbe55c 0B / 240B 5.3s
2023-12-02 05:25:42.341Z: #4 sha256:59d5b1cf8ef097657e4c2157443131e4e14997efb3a0042f4f7bd43bc4c8d566 12.21MB / 60.61MB 5.4s2023-12-02 05:25:42.343Z: 
#4 sha256:9da9948bb761fa37083d3c9a1fd71e7e3a93951fb0786bf3cab014068fbbe55c 240B / 240B 5.4s done
#4 sha256:cdb217fcffc2286bc4a98dd2a882800210e9563cac126d6be43c3c92aad2d720 1.99MB / 1.99MB 5.4s
2023-12-02 05:25:42.469Z: #4 sha256:59d5b1cf8ef097657e4c2157443131e4e14997efb3a0042f4f7bd43bc4c8d566 30.41MB / 60.61MB 5.6s
#4 sha256:cdb217fcffc2286bc4a98dd2a882800210e9563cac126d6be43c3c92aad2d720 1.99MB / 1.99MB 5.5s done
#4 sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 8.39MB / 99.55MB 5.6s
2023-12-02 05:25:42.619Z: #4 sha256:59d5b1cf8ef097657e4c2157443131e4e14997efb3a0042f4f7bd43bc4c8d566 33.55MB / 60.61MB 5.7s
#4 sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 16.78MB / 99.55MB 5.7s
2023-12-02 05:25:42.768Z: #4 sha256:59d5b1cf8ef097657e4c2157443131e4e14997efb3a0042f4f7bd43bc4c8d566 50.33MB / 60.61MB 5.9s
#4 sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 33.73MB / 99.55MB 5.9s
2023-12-02 05:25:42.883Z: #4 sha256:59d5b1cf8ef097657e4c2157443131e4e14997efb3a0042f4f7bd43bc4c8d566 60.61MB / 60.61MB 6.1s
#4 sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 45.09MB / 99.55MB 6.1s
2023-12-02 05:25:43.167Z: #4 sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 57.67MB / 99.55MB 6.3s2023-12-02 05:25:43.180Z: 
2023-12-02 05:25:43.270Z: #4 sha256:59d5b1cf8ef097657e4c2157443131e4e14997efb3a0042f4f7bd43bc4c8d566 60.61MB / 60.61MB 6.4s done
#4 sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 69.21MB / 99.55MB 6.4s
2023-12-02 05:25:43.420Z: #4 extracting sha256:ddf874abf16cc990e0fd75a154a34ca0a03ee310ad895a18fb62ae15bf4171fb 5.1s
#4 sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 75.50MB / 99.55MB 6.5s
2023-12-02 05:25:43.668Z: #4 sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 98.57MB / 99.55MB 6.8s2023-12-02 05:25:43.677Z: 
2023-12-02 05:25:44.063Z: #4 extracting sha256:ddf874abf16cc990e0fd75a154a34ca0a03ee310ad895a18fb62ae15bf4171fb 5.8s done2023-12-02 05:25:44.068Z: 
2023-12-02 05:25:44.313Z: #4 sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 99.55MB / 99.55MB 7.4s done
2023-12-02 05:25:44.464Z: #4 extracting sha256:5c1459d3ab8b5e46ac1a0a00134fe2f7b693474eb6d75ace97ecbe811a6f5b0e
2023-12-02 05:25:44.961Z: #4 extracting sha256:5c1459d3ab8b5e46ac1a0a00134fe2f7b693474eb6d75ace97ecbe811a6f5b0e 0.5s done
2023-12-02 05:25:46.017Z: #4 extracting sha256:9a11a33b016bcaf1d0bd4a0857c13c9dc9486d5eb19d808d5c237d0cb271b99a done
2023-12-02 05:25:46.167Z: #4 extracting sha256:b837e19a13f10adaa26316a877e8a3b54df5cf7543914009d2ee02b41d64378f done
2023-12-02 05:25:46.318Z: #4 extracting sha256:be88e9b1429e6abe1be4803e5f9560c271a407bd97941c12e81be9025abdab2d done
2023-12-02 05:25:46.468Z: #4 extracting sha256:469dc137be941824529e4f076cc2bbc129231c822962ad32580a4e2cd452253c done
2023-12-02 05:25:46.571Z: #4 extracting sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d
2023-12-02 05:25:51.681Z: #4 extracting sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 5.1s done2023-12-02 05:25:51.690Z: 
2023-12-02 05:25:53.024Z: #4 extracting sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca12023-12-02 05:25:53.032Z: 
2023-12-02 05:25:58.142Z: #4 extracting sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 5.0s done
2023-12-02 05:25:59.919Z: #4 extracting sha256:f7abe09e5d5e4def17605244e9a4f2e8203b1d8d544fa30396d5ec42e6c47bf9
2023-12-02 05:26:00.064Z: #4 extracting sha256:f7abe09e5d5e4def17605244e9a4f2e8203b1d8d544fa30396d5ec42e6c47bf9 done
2023-12-02 05:26:00.214Z: #4 extracting sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681
2023-12-02 05:26:04.911Z: #4 extracting sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 4.8s done2023-12-02 05:26:04.914Z: 
2023-12-02 05:26:07.467Z: #4 extracting sha256:857523023f3af2b5bd1a8e05e269fa461162a454beb866f2e32551c7356fd0b8 done
2023-12-02 05:26:07.617Z: #4 extracting sha256:af0f8691d92b92416b19654d847770431abe5077d51bd1f815dcdf834804ff22 done
2023-12-02 05:26:07.768Z: #4 extracting sha256:a5f5243ec26f765b90acd2506eb615faaed46a306c1f5a1804b434b72cc8435c
2023-12-02 05:26:09.323Z: #4 extracting sha256:a5f5243ec26f765b90acd2506eb615faaed46a306c1f5a1804b434b72cc8435c 1.5s done
2023-12-02 05:26:10.061Z: #4 extracting sha256:af7055f83fa381583c03a343562a0c407db2d45bd28d4e323034c8f06d2f2a2e
2023-12-02 05:26:10.207Z: #4 extracting sha256:af7055f83fa381583c03a343562a0c407db2d45bd28d4e323034c8f06d2f2a2e done
2023-12-02 05:26:10.357Z: #4 extracting sha256:1fbeb5db8b38e923a081350f3d836fb3b593c83f50566f296561558143d16f11 done
2023-12-02 05:26:10.508Z: #4 extracting sha256:f130883feb0eb350abe241dc9409fb73dd51704ad3ae92b536563eb149b33346 done
2023-12-02 05:26:10.659Z: #4 extracting sha256:4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1 done
2023-12-02 05:26:10.809Z: #4 extracting sha256:7ec8d5cae060f1455aec6189e1de7858b03dc8073c461a5e717fed7c336d28b8 done
2023-12-02 05:26:10.960Z: #4 extracting sha256:9da9948bb761fa37083d3c9a1fd71e7e3a93951fb0786bf3cab014068fbbe55c done
2023-12-02 05:26:11.061Z: #4 extracting sha256:59d5b1cf8ef097657e4c2157443131e4e14997efb3a0042f4f7bd43bc4c8d5662023-12-02 05:26:11.064Z: 
2023-12-02 05:26:13.008Z: #4 extracting sha256:59d5b1cf8ef097657e4c2157443131e4e14997efb3a0042f4f7bd43bc4c8d566 1.8s done2023-12-02 05:26:13.013Z: 
2023-12-02 05:26:13.744Z: #4 extracting sha256:cdb217fcffc2286bc4a98dd2a882800210e9563cac126d6be43c3c92aad2d7202023-12-02 05:26:13.749Z: 
2023-12-02 05:26:14.115Z: #4 extracting sha256:cdb217fcffc2286bc4a98dd2a882800210e9563cac126d6be43c3c92aad2d720 0.2s done
2023-12-02 05:26:14.408Z: #4 extracting sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 0.1s
2023-12-02 05:26:18.953Z: #4 extracting sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 4.7s done2023-12-02 05:26:18.957Z: 
2023-12-02 05:26:23.729Z: #4 DONE 47.1s
2023-12-02 05:26:23.879Z: 
#6 [dev_container_auto_added_stage_label 2/3] COPY ../codespaces/demoVE.yml* ../codespaces/noop.txt /tmp/conda-tmp/
2023-12-02 05:26:24.029Z: #6 DONE 0.2s

#7 [dev_container_auto_added_stage_label 3/3] RUN if [ -f "/tmp/conda-tmp/demoVE.yml" ]; then umask 0002 && /opt/conda/bin/conda env create -f /tmp/conda-tmp/demoVE.yml; fi     && rm -rf /tmp/conda-tmp
2023-12-02 05:26:25.382Z: #7 1.364 Collecting package metadata (repodata.json): ...working... 2023-12-02 05:27:41.248Z: done2023-12-02 05:27:41.255Z: 
#7 77.33 Solving environment: ...working... 2023-12-02 05:27:43.802Z: done
2023-12-02 05:27:43.954Z: #7 79.97 2023-12-02 05:27:43.958Z: 
#7 79.97 
#7 79.97 ==> WARNING: A newer version of conda exists. <==
#7 79.97   current version: 23.9.0
2023-12-02 05:27:43.964Z: #7 79.97   latest version: 23.10.0
#7 79.97 
#7 79.97 Please update conda by running
#7 79.97 
#7 79.97     $ conda update -n base -c defaults conda
#7 79.97 
#7 79.97 Or to minimize the number of packages updated during conda update use
#7 79.97 
#7 79.97      conda install conda=23.10.0
#7 79.97 
#7 79.97 
2023-12-02 05:27:47.261Z: #7 83.21 2023-12-02 05:27:47.267Z: 
2023-12-02 05:27:47.271Z: #7 83.21 Downloading and Extracting Packages: ...working... done
#7 83.21 Preparing transaction: ...working... 2023-12-02 05:27:47.411Z: done
#7 83.38 Verifying transaction: ...working... 2023-12-02 05:27:48.463Z: done
#7 84.44 Executing transaction: ...working... 2023-12-02 05:27:51.168Z: done
2023-12-02 05:27:51.469Z: #7 87.43 Installing pip dependencies: ...working... 2023-12-02 05:28:10.271Z: Ran pip subprocess with arguments:
2023-12-02 05:28:10.275Z: #7 106.2 ['/opt/conda/envs/demoVE/bin/python', '-m', 'pip', 'install', '-U', '-r', '/tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt', '--exists-action=b']
#7 106.2 Pip subprocess output:
#7 106.2 Collecting opencv-python-headless (from -r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 1))
#7 106.2   Downloading opencv_python_headless-4.8.1.78-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (19 kB)
#7 106.2 Collecting ipykernel (from -r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
#7 106.2   Downloading ipykernel-6.27.1-py3-none-any.whl.metadata (6.3 kB)
#7 106.2 Collecting matplotlib (from -r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 3))
#7 106.2   Downloading matplotlib-3.8.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.8 kB)
#7 106.2 Collecting numpy>=1.21.2 (from opencv-python-headless->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 1))
#7 106.2   Downloading numpy-1.26.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (61 kB)
#7 106.2      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.2/61.2 kB 1.8 MB/s eta 0:00:00
#7 106.2 Collecting comm>=0.1.1 (from ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
2023-12-02 05:28:10.321Z: #7 106.2   Downloading comm-0.2.0-py3-none-any.whl.metadata (3.7 kB)
#7 106.2 Collecting debugpy>=1.6.5 (from ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
#7 106.2   Downloading debugpy-1.8.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (1.0 kB)
#7 106.2 Collecting ipython>=7.23.1 (from ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
#7 106.2   Downloading ipython-8.18.1-py3-none-any.whl.metadata (6.0 kB)
#7 106.2 Collecting jupyter-client>=6.1.12 (from ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
2023-12-02 05:28:10.326Z: #7 106.2   Downloading jupyter_client-8.6.0-py3-none-any.whl.metadata (8.3 kB)
#7 106.2 Collecting jupyter-core!=5.0.*,>=4.12 (from ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
#7 106.2   Downloading jupyter_core-5.5.0-py3-none-any.whl.metadata (3.4 kB)2023-12-02 05:28:10.331Z: 
#7 106.2 Collecting matplotlib-inline>=0.1 (from ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
#7 106.2   Downloading matplotlib_inline-0.1.6-py3-none-any.whl (9.4 kB)
2023-12-02 05:28:10.334Z: #7 106.2 Collecting nest-asyncio (from ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
#7 106.2   Downloading nest_asyncio-1.5.8-py3-none-any.whl.metadata (2.8 kB)
#7 106.2 Collecting packaging (from ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
2023-12-02 05:28:10.338Z: #7 106.2   Downloading packaging-23.2-py3-none-any.whl.metadata (3.2 kB)
#7 106.2 Collecting psutil (from ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
2023-12-02 05:28:10.342Z: #7 106.2   Downloading psutil-5.9.6-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (21 kB)
#7 106.2 Collecting pyzmq>=20 (from ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
2023-12-02 05:28:10.347Z: #7 106.2   Downloading pyzmq-25.1.1-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (4.9 kB)
#7 106.2 Collecting tornado>=6.1 (from ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
#7 106.2   Downloading tornado-6.4-cp38-abi3-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.5 kB)
2023-12-02 05:28:10.350Z: #7 106.2 Collecting traitlets>=5.4.0 (from ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
#7 106.2   Downloading traitlets-5.14.0-py3-none-any.whl.metadata (10 kB)
#7 106.2 Collecting contourpy>=1.0.1 (from matplotlib->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 3))
2023-12-02 05:28:10.355Z: #7 106.2   Downloading contourpy-1.2.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.8 kB)
#7 106.2 Collecting cycler>=0.10 (from matplotlib->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 3))
2023-12-02 05:28:10.358Z: #7 106.2   Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
#7 106.2 Collecting fonttools>=4.22.0 (from matplotlib->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 3))
2023-12-02 05:28:10.362Z: #7 106.2   Downloading fonttools-4.45.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (155 kB)
#7 106.2      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 155.2/155.2 kB 967.6 kB/s eta 0:00:00
#7 106.2 Collecting kiwisolver>=1.3.1 (from matplotlib->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 3))
2023-12-02 05:28:10.365Z: #7 106.2   Downloading kiwisolver-1.4.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.4 kB)
#7 106.2 Collecting pillow>=8 (from matplotlib->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 3))
#7 106.2   Downloading Pillow-10.1.0-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (9.5 kB)2023-12-02 05:28:10.370Z: 
#7 106.2 Collecting pyparsing>=2.3.1 (from matplotlib->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 3))
#7 106.2   Downloading pyparsing-3.1.1-py3-none-any.whl.metadata (5.1 kB)
2023-12-02 05:28:10.373Z: #7 106.2 Collecting python-dateutil>=2.7 (from matplotlib->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 3))
#7 106.2   Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
#7 106.2      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 247.7/247.7 kB 7.3 MB/s eta 0:00:002023-12-02 05:28:10.377Z: 
#7 106.2 Collecting decorator (from ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
#7 106.2   Downloading decorator-5.1.1-py3-none-any.whl (9.1 kB)
2023-12-02 05:28:10.380Z: #7 106.2 Collecting jedi>=0.16 (from ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
#7 106.2   Downloading jedi-0.19.1-py2.py3-none-any.whl.metadata (22 kB)
#7 106.2 Collecting prompt-toolkit<3.1.0,>=3.0.41 (from ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))2023-12-02 05:28:10.385Z: 
#7 106.2   Downloading prompt_toolkit-3.0.41-py3-none-any.whl.metadata (6.5 kB)
#7 106.2 Collecting pygments>=2.4.0 (from ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))2023-12-02 05:28:10.389Z: 
#7 106.2   Downloading pygments-2.17.2-py3-none-any.whl.metadata (2.6 kB)
#7 106.2 Collecting stack-data (from ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
#7 106.2   Downloading stack_data-0.6.3-py3-none-any.whl.metadata (18 kB)2023-12-02 05:28:10.393Z: 
#7 106.2 Collecting pexpect>4.3 (from ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
#7 106.2   Downloading pexpect-4.9.0-py2.py3-none-any.whl.metadata (2.5 kB)
2023-12-02 05:28:10.397Z: #7 106.2 Collecting platformdirs>=2.5 (from jupyter-core!=5.0.*,>=4.12->ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
#7 106.2   Downloading platformdirs-4.0.0-py3-none-any.whl.metadata (11 kB)
2023-12-02 05:28:10.402Z: #7 106.2 Collecting six>=1.5 (from python-dateutil>=2.7->matplotlib->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 3))
#7 106.2   Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
#7 106.2 Collecting parso<0.9.0,>=0.8.3 (from jedi>=0.16->ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))2023-12-02 05:28:10.406Z: 
#7 106.2   Downloading parso-0.8.3-py2.py3-none-any.whl (100 kB)
#7 106.2      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.8/100.8 kB 3.1 MB/s eta 0:00:00
2023-12-02 05:28:10.410Z: #7 106.2 Collecting ptyprocess>=0.5 (from pexpect>4.3->ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
#7 106.2   Downloading ptyprocess-0.7.0-py2.py3-none-any.whl (13 kB)
#7 106.2 Collecting wcwidth (from prompt-toolkit<3.1.0,>=3.0.41->ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))2023-12-02 05:28:10.414Z: 
#7 106.2   Downloading wcwidth-0.2.12-py2.py3-none-any.whl.metadata (14 kB)
#7 106.2 Collecting executing>=1.2.0 (from stack-data->ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
2023-12-02 05:28:10.418Z: #7 106.2   Downloading executing-2.0.1-py2.py3-none-any.whl.metadata (9.0 kB)
#7 106.2 Collecting asttokens>=2.1.0 (from stack-data->ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
#7 106.2   Downloading asttokens-2.4.1-py2.py3-none-any.whl.metadata (5.2 kB)2023-12-02 05:28:10.422Z: 
#7 106.2 Collecting pure-eval (from stack-data->ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.a7qvq18x.requirements.txt (line 2))
#7 106.2   Downloading pure_eval-0.2.2-py3-none-any.whl (11 kB)2023-12-02 05:28:10.426Z: 
#7 106.2 Downloading opencv_python_headless-4.8.1.78-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (49.1 MB)
#7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 49.1/49.1 MB 23.6 MB/s eta 0:00:00
2023-12-02 05:28:10.429Z: #7 106.2 Downloading ipykernel-6.27.1-py3-none-any.whl (114 kB)
#7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 114.6/114.6 kB 3.5 MB/s eta 0:00:00
#7 106.2 Downloading matplotlib-3.8.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.6 MB)
2023-12-02 05:28:10.434Z: #7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.6/11.6 MB 51.9 MB/s eta 0:00:00
#7 106.2 Downloading comm-0.2.0-py3-none-any.whl (7.0 kB)
2023-12-02 05:28:10.436Z: #7 106.2 Downloading contourpy-1.2.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (313 kB)
#7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 313.4/313.4 kB 9.3 MB/s eta 0:00:00
#7 106.2 Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)2023-12-02 05:28:10.441Z: 
#7 106.2 Downloading debugpy-1.8.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
#7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 37.4 MB/s eta 0:00:00
2023-12-02 05:28:10.445Z: #7 106.2 Downloading fonttools-4.45.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.9 MB)
#7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.9/4.9 MB 24.2 MB/s eta 0:00:00
#7 106.2 Downloading ipython-8.18.1-py3-none-any.whl (808 kB)
2023-12-02 05:28:10.449Z: #7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 808.2/808.2 kB 19.8 MB/s eta 0:00:00
#7 106.2 Downloading jupyter_client-8.6.0-py3-none-any.whl (105 kB)
2023-12-02 05:28:10.453Z: #7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 105.9/105.9 kB 3.3 MB/s eta 0:00:00
#7 106.2 Downloading jupyter_core-5.5.0-py3-none-any.whl (28 kB)
#7 106.2 Downloading kiwisolver-1.4.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.4 MB)2023-12-02 05:28:10.457Z: 
#7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.4/1.4 MB 25.8 MB/s eta 0:00:00
#7 106.2 Downloading numpy-1.26.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (18.2 MB)
#7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 18.2/18.2 MB 42.8 MB/s eta 0:00:002023-12-02 05:28:10.461Z: 
#7 106.2 Downloading packaging-23.2-py3-none-any.whl (53 kB)
#7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 53.0/53.0 kB 1.5 MB/s eta 0:00:00
2023-12-02 05:28:10.464Z: #7 106.2 Downloading Pillow-10.1.0-cp311-cp311-manylinux_2_28_x86_64.whl (3.6 MB)
#7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.6/3.6 MB 47.4 MB/s eta 0:00:00
2023-12-02 05:28:10.468Z: #7 106.2 Downloading pyparsing-3.1.1-py3-none-any.whl (103 kB)
#7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.1/103.1 kB 3.1 MB/s eta 0:00:00
#7 106.2 Downloading pyzmq-25.1.1-cp311-cp311-manylinux_2_28_x86_64.whl (1.1 MB)
2023-12-02 05:28:10.472Z: #7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 23.3 MB/s eta 0:00:00
#7 106.2 Downloading tornado-6.4-cp38-abi3-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (435 kB)
#7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 435.4/435.4 kB 12.4 MB/s eta 0:00:00
2023-12-02 05:28:10.475Z: #7 106.2 Downloading traitlets-5.14.0-py3-none-any.whl (85 kB)
#7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 85.2/85.2 kB 2.3 MB/s eta 0:00:00
2023-12-02 05:28:10.479Z: #7 106.2 Downloading nest_asyncio-1.5.8-py3-none-any.whl (5.3 kB)
#7 106.2 Downloading psutil-5.9.6-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (283 kB)
#7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 283.6/283.6 kB 8.8 MB/s eta 0:00:002023-12-02 05:28:10.483Z: 
#7 106.2 Downloading jedi-0.19.1-py2.py3-none-any.whl (1.6 MB)
#7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 32.1 MB/s eta 0:00:00
2023-12-02 05:28:10.487Z: #7 106.2 Downloading pexpect-4.9.0-py2.py3-none-any.whl (63 kB)
#7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.8/63.8 kB 2.0 MB/s eta 0:00:00
#7 106.2 Downloading platformdirs-4.0.0-py3-none-any.whl (17 kB)2023-12-02 05:28:10.491Z: 
#7 106.2 Downloading prompt_toolkit-3.0.41-py3-none-any.whl (385 kB)
#7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 385.5/385.5 kB 10.8 MB/s eta 0:00:00
2023-12-02 05:28:10.495Z: #7 106.2 Downloading pygments-2.17.2-py3-none-any.whl (1.2 MB)
#7 106.2    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 24.7 MB/s eta 0:00:00
#7 106.2 Downloading stack_data-0.6.3-py3-none-any.whl (24 kB)2023-12-02 05:28:10.500Z: 
#7 106.2 Downloading asttokens-2.4.1-py2.py3-none-any.whl (27 kB)
#7 106.2 Downloading executing-2.0.1-py2.py3-none-any.whl (24 kB)
#7 106.2 Downloading wcwidth-0.2.12-py2.py3-none-any.whl (34 kB)2023-12-02 05:28:10.502Z: 
#7 106.2 Installing collected packages: wcwidth, pure-eval, ptyprocess, traitlets, tornado, six, pyzmq, pyparsing, pygments, psutil, prompt-toolkit, platformdirs, pillow, pexpect, parso, packaging, numpy, nest-asyncio, kiwisolver, fonttools, executing, decorator, debugpy, cycler, python-dateutil, opencv-python-headless, matplotlib-inline, jupyter-core, jedi, contourpy, comm, asttokens, stack-data, matplotlib, jupyter-client, ipython, ipykernel
#7 106.2 Successfully installed asttokens-2.4.1 comm-0.2.0 contourpy-1.2.0 cycler-0.12.1 debugpy-1.8.0 decorator-5.1.1 executing-2.0.1 fonttools-4.45.1 ipykernel-6.27.1 ipython-8.18.1 jedi-0.19.1 jupyter-client-8.6.0 jupyter-core-5.5.0 kiwisolver-1.4.5 matplotlib-3.8.2 matplotlib-inline-0.1.6 nest-asyncio-1.5.8 numpy-1.26.2 opencv-python-headless-4.8.1.78 packaging-23.2 parso-0.8.3 pexpect-4.9.0 pillow-10.1.0 platformdirs-4.0.0 prompt-toolkit-3.0.41 psutil-5.9.6 ptyprocess-0.7.0 pure-eval-0.2.2 pygments-2.17.2 pyparsing-3.1.1 python-dateutil-2.8.2 pyzmq-25.1.1 six-1.16.0 stack-data-0.6.3 tornado-6.4 traitlets-5.14.0 wcwidth-0.2.122023-12-02 05:28:10.505Z: 
#7 106.2 
#7 106.2 done
#7 106.2 #2023-12-02 05:28:10.510Z: 
#7 106.2 # To activate this environment, use
#7 106.2 #
2023-12-02 05:28:10.515Z: #7 106.2 #     $ conda activate demoVE
#7 106.2 #
2023-12-02 05:28:10.517Z: #7 106.2 # To deactivate an active environment, use
#7 106.2 #
2023-12-02 05:28:10.520Z: #7 106.2 #     $ conda deactivate
#7 106.2 
2023-12-02 05:28:17.776Z: #7 DONE 113.7s

#8 preparing layers for inline cache
2023-12-02 05:28:28.998Z: #8 DONE 11.3s

#9 exporting to image
#9 exporting layers done
#9 writing image sha256:452422467e7c86fc272e0894f751686094d58432d83271aa854569a5a2e92f48 0.0s done
#9 naming to docker.io/library/vsc-code-ebc7ff1bb830c9ab527f890f7f31279e8e4979e92a94006398168157f6921606 0.0s done
2023-12-02 05:28:29.001Z: #9 DONE 0.1s
2023-12-02 05:28:29.013Z: Stop: Run: docker buildx build --load --build-arg BUILDKIT_INLINE_CACHE=1 -f /tmp/devcontainercli-root/container-features/0.52.1-1701494735276/Dockerfile-with-features -t vsc-code-ebc7ff1bb830c9ab527f890f7f31279e8e4979e92a94006398168157f6921606 --target dev_containers_target_stage --build-arg _DEV_CONTAINERS_BASE_IMAGE=dev_container_auto_added_stage_label /var/lib/docker/codespacemount/workspace/code
2023-12-02 05:28:29.043Z: $127.0.0.1 --cap-add sys_nice --network host --entrypoint /bin/sh vsc-code-ebc7ff1bb830c9ab527f890f7f31279e8e4979e92a94006398168157f6921606 -c echo Container started
2023-12-02 05:28:29.369Z: Container started
2023-12-02 05:28:29.715Z: Outcome: success User: vscode WorkspaceFolder: /workspaces/code
2023-12-02 05:28:29.721Z: devcontainer process exited with exit code 0

=================================================================================
2023-12-02 05:28:30.993Z: Running blocking commands...
2023-12-02 05:28:31.023Z: $ devcontainer up --id-label Type=codespaces --workspace-folder /var/lib/docker/codespacemount/workspace/code --mount type=bind,source=/.codespaces/agent/mount/cache,target=/vscode --user-data-folder /var/lib/docker/codespacemount/.persistedshare --container-data-folder .vscode-remote/data/Machine --container-system-data-folder /var/vscode-remote --log-level trace --log-format json --update-remote-user-uid-default never --mount-workspace-git-root false --omit-config-remote-env-from-metadata --skip-non-blocking-commands --expect-existing-container --config "/var/lib/docker/codespacemount/workspace/code/.devcontainer/devcontainer.json" --override-config /root/.codespaces/shared/merged_devcontainer.json --default-user-env-probe loginInteractiveShell --container-session-data-folder /workspaces/.codespaces/.persistedshare/devcontainers-cli/cache --secrets-file /root/.codespaces/shared/user-secrets-envs.json
2023-12-02 05:28:31.268Z: @devcontainers/cli 0.52.1. Node.js v18.17.1. linux 6.2.0-1016-azure x64.
2023-12-02 05:28:31.591Z: Outcome: success User: vscode WorkspaceFolder: /workspaces/code
2023-12-02 05:28:31.607Z: devcontainer process exited with exit code 0

=================================================================================
2023-12-02 05:28:32.008Z: Configuring codespace...
2023-12-02 05:28:32.017Z: $ cp -r /root/.docker /var/lib/docker/codespacemount/.persistedshare
2023-12-02 05:28:32.037Z: cp process exited with exit code 0
2023-12-02 05:28:32.084Z: $ rm -rf /home/vscode/.docker
2023-12-02 05:28:32.143Z: rm process exited with exit code 0
2023-12-02 05:28:32.382Z: $ ln -sfn /workspaces/.codespaces/.persistedshare/.docker /home/vscode/.docker
2023-12-02 05:28:32.608Z: ln process exited with exit code 0
2023-12-02 05:28:32.631Z: $ chown -R vscode /workspaces/.codespaces/.persistedshare/.docker
2023-12-02 05:28:32.635Z: chown process exited with exit code 0

=================================================================================
2023-12-02 05:28:32.640Z: Running commands...
2023-12-02 05:28:32.658Z: $ devcontainer up --id-label Type=codespaces --workspace-folder /var/lib/docker/codespacemount/workspace/code --expect-existing-container --skip-post-attach --mount type=bind,source=/.codespaces/agent/mount/cache,target=/vscode --container-data-folder .vscode-remote/data/Machine --container-system-data-folder /var/vscode-remote --log-level trace --log-format json --update-remote-user-uid-default never --mount-workspace-git-root false --config "/var/lib/docker/codespacemount/workspace/code/.devcontainer/devcontainer.json" --override-config /root/.codespaces/shared/merged_devcontainer.json --default-user-env-probe loginInteractiveShell --container-session-data-folder /workspaces/.codespaces/.persistedshare/devcontainers-cli/cache --secrets-file /root/.codespaces/shared/user-secrets-envs.json
2023-12-02 05:28:33.054Z: @devcontainers/cli 0.52.1. Node.js v18.17.1. linux 6.2.0-1016-azure x64.
2023-12-02 05:28:33.483Z: Running the postCreateCommand from devcontainer.json...

2023-12-02 05:28:33.500Z: conda init
2023-12-02 05:28:34.905Z: no change     /opt/conda/condabin/conda
no change     /opt/conda/bin/conda
no change     /opt/conda/bin/conda-env
no change     /opt/conda/bin/activate
no change     /opt/conda/bin/deactivate
no change     /opt/conda/etc/profile.d/conda.sh
no change     /opt/conda/etc/fish/conf.d/conda.fish
no change     /opt/conda/shell/condabin/Conda.psm1
no change     /opt/conda/shell/condabin/conda-hook.ps1
no change     /opt/conda/lib/python3.11/site-packages/xontrib/conda.xsh
no change     /opt/conda/etc/profile.d/conda.csh
modified      /home/vscode/.bashrc=> For changes to take effect, close and re-open your current shell. <==

2023-12-02 05:28:34.978Z: Outcome: success User: vscode WorkspaceFolder: /workspaces/code
2023-12-02 05:28:34.995Z: devcontainer process exited with exit code 0

=================================================================================
2023-12-02 05:28:35.039Z: Finished configuring codespace.

```
